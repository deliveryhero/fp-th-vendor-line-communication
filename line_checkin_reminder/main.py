import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_v2
from get_secrete_token import get_secret_data
import datetime, pytz
import requests
from template import json_object

# Basic configuration tables
query_table = "foodpanda-th-bigquery.pandata_th.country_TH_vendor_experience_line_checkin_reminder"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

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
      SELECT DISTINCT
        vendor_code,
        "Uca11d4d4585c435204950dba18dafcd8" AS line_user_id
      FROM {query_table}
      WHERE line_user_id IS NOT NULL
        AND DATE(recorded_at_local) = CURRENT_DATE("Asia/Bangkok")
        AND opening_time >= TIME_SUB(TIME(CURRENT_DATETIME("Asia/Bangkok")), INTERVAL 30 MINUTE)
        AND opening_time <= TIME(CURRENT_DATETIME("Asia/Bangkok"))
      LIMIT 1
    """

if Live == True:
    query = f"""
      SELECT DISTINCT
        vendor_code,
        line_user_id
      FROM {query_table}
      WHERE line_user_id IS NOT NULL
        AND DATE(recorded_at_local) = CURRENT_DATE("Asia/Bangkok")
        AND opening_time >= TIME_SUB(TIME(CURRENT_DATETIME("Asia/Bangkok")), INTERVAL 30 MINUTE)
        AND opening_time <= TIME(CURRENT_DATETIME("Asia/Bangkok"))
    """

try:
  dataframe = query_BQ_table(query)
  # print("Created dataframe successfully")
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_checkin_reminder*: Failed to get data: ' + str(e)})
  # print("Cannot create dataframe")
  # print(e)

try:
  reponse_code_list, json_list = send_request_line_api_v2(url = url,
                                                          headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_checkin_reminder*: Failed send API request: ' + str(e)})

df = dataframe.filter(items=['vendor_code', 'line_user_id'])
df["return_response"] = reponse_code_list
df["msg_sent_date_time"] = now
df["template_id_if_any"] = "line_checkin_reminder"
df["msg_url"] = url
df["msg_content"] = "line_checkin_reminder"
df_records = df.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_checkin_reminder*: Failed to record logs: ' + str(e)})
  # print(e)
