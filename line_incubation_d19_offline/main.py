import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_generic_reminder
from get_secrete_token import get_secret_data
import datetime, pytz
import requests
from template import json_object

# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_ops_incubation_line_verification"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"
pipeline_name = "line_incubation_d19_offline"
vendor_age = 19

# Basic configuration parameters
slack_webhook = os.getenv('slack_webhook')
Live = False
url = "https://api.line.me/v2/bot/message/push"

token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}", 'Content-Type': 'application/json'}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
      SELECT
        vendor_code,
        "Uca11d4d4585c435204950dba18dafcd8" AS line_user_id,
        vendor_age
      FROM `{query_table}`
      WHERE line_user_id IS NOT NULL
        AND vendor_age = {vendor_age}
        AND vertical = "Restaurant"
      LIMIT 1
    """

if Live == True:
    query = f"""
      SELECT
        vendor_code,
        line_user_id,
        vendor_age
      FROM `{query_table}`
      WHERE line_user_id IS NOT NULL
        AND vendor_age = {vendor_age}
        AND vertical = "Restaurant"
        AND DATE(recorded_at_local) = CURRENT_DATE("Asia/Bangkok")
    """

try:
  dataframe = query_BQ_table(query)
  # print("Created dataframe successfully")
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*{pipeline_name}*: Failed to get data: ' + str(e)})
  # print("Cannot create dataframe")
  # print(e)

try:
  reponse_code_list, json_list = send_request_line_api_generic_reminder(url = url,
                                                          headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*{pipeline_name}*: Failed send API request: ' + str(e)})

df = dataframe.filter(items=['vendor_code', 'line_user_id'])
df["return_response"] = reponse_code_list
df["msg_sent_date_time"] = now
df["template_id_if_any"] = pipeline_name
df["msg_url"] = url
df["msg_content"] = pipeline_name
df_records = df.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*{pipeline_name}*: Failed to record logs: ' + str(e)})
  # print(e)
