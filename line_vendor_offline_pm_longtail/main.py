import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_v5
from get_secrete_token import get_secret_data
import datetime, pytz
import requests
from template import json_object

# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_auto_vendor_offline_pm_longtail"
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
      SELECT DISTINCT
        vendor_code,
        vendor_name,
        start_date_in_thai,
        end_date_in_thai,
        'U2b9495e231b925da2ed4163beeef6dad' AS line_user_id,
        CAST(total_offline_hours AS STRING) AS total_offline_hours,
        CAST(potential_order_loss AS STRING) AS potential_order_loss
      FROM {query_table}
      WHERE line_user_id IS NOT NULL
        AND DATE(recorded_at_local) = CURRENT_DATE
      LIMIT 1
    """

if Live == True:
    query = f"""
      SELECT DISTINCT
        vendor_code,
        vendor_name,
        start_date_in_thai,
        end_date_in_thai,
        line_user_id,
        CAST(total_offline_hours AS STRING) AS total_offline_hours,
        CAST(potential_order_loss AS STRING) AS potential_order_loss
      FROM {query_table}
      WHERE line_user_id IS NOT NULL
        AND DATE(recorded_at_local) = CURRENT_DATE
    """

try:
  dataframe = query_BQ_table(query)
  # print("Created dataframe successfully")
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_vendor_offline_pm_longtail*: Failed to get data: ' + str(e)})
  # print("Cannot create dataframe")
  # print(e)

try:
  reponse_code_list, json_list = send_request_line_api_v5(url = url, 
                                                          headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_vendor_offline_pm_longtail*: Failed send API request: ' + str(e)})

try:
  df = dataframe.filter(items=['vendor_code', 'line_user_id'])
  df["return_response"] = reponse_code_list
  df["msg_sent_date_time"] = now
  df["template_id_if_any"] = "line_vendor_offline_pm_longtail"
  df["msg_url"] = url
  df["msg_content"] = 'content vendor_name: ' + dataframe['vendor_name'] \
                      +','+'content start_date_in_thai: ' + dataframe['start_date_in_thai'] \
                      +','+'content end_date_in_thai: ' + dataframe['end_date_in_thai'] \
                      +','+'content total_offline_hours: ' + dataframe['total_offline_hours'] \
                      +','+'content potential_order_loss: ' + dataframe['potential_order_loss']
  df_records = df.to_dict('records')
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_vendor_offline_pm_longtail*: Failed to record logs: ' + str(e)})
  # print(e)
