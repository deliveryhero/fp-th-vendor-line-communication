import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_rider_late_communication
from get_secrete_token import get_secret_data
import datetime, pytz
import requests
from template import json_object

# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_auto_rider_late_communication"
line_data  = "foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

# Basic configuration parameters
slack_webhook = os.getenv('slack_webhook')
Live = True
url = "https://api.line.me/v2/bot/message/push"

token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}", 'Content-Type': 'application/json'}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
    SELECT 
      rider_late.vendor_code,
      "U2b9495e231b925da2ed4163beeef6dad" AS line_user_id
    FROM `fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_auto_rider_late_communication` AS rider_late
    INNER JOIN `foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup` AS line_data
            ON LOWER(rider_late.vendor_code) = LOWER(line_data.VendorCode)
    QUALIFY ROW_NUMBER() OVER (PARTITION BY rider_late.vendor_code, line_data.LineUserID) = 1
    LIMIT 1
    """

if Live == True:
    query = f"""
      SELECT 
        rider_late.vendor_code,
        line_data.LineUserID AS line_user_id
      FROM `fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_auto_rider_late_communication` AS rider_late
      INNER JOIN `foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup` AS line_data
              ON LOWER(rider_late.vendor_code) = LOWER(line_data.VendorCode)
      QUALIFY ROW_NUMBER() OVER (PARTITION BY rider_late.vendor_code, line_data.LineUserID) = 1
    """

try:
  dataframe = query_BQ_table(query)
  # print("Created dataframe successfully")
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_vendor_rider_late_communication*: Failed to get data: ' + str(e)})
  # print("Cannot create dataframe")
  # print(e)

try:
  reponse_code_list, json_list = send_request_line_api_rider_late_communication(url = url,
                                                          headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_vendor_rider_late_communication*: Failed send API request: ' + str(e)})

try:
  df = dataframe.filter(items=['vendor_code', 'line_user_id'])
  df["return_response"] = reponse_code_list
  df["msg_sent_date_time"] = now
  df["template_id_if_any"] = "line_vendor_rider_late_communication"
  df["msg_url"] = url
  df["msg_content"] = "line_vendor_rider_late_communication"
  df_records = df.to_dict('records')
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_vendor_rider_late_communication*: Failed to record logs: ' + str(e)})
  # print(e)
