import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_v6
from get_secrete_token import get_secret_data
import datetime, pytz
import requests
from template import json_object

# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_auto_vendor_offline_skam"
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
      'Ucd25fe3518e5cda83a0e704446b1ef08' AS line_user_id,
      total_offline_hours
    FROM {query_table}
    WHERE line_user_id IS NOT NULL
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
      total_offline_hours
    FROM {query_table}
    WHERE line_user_id IS NOT NULL
    """

try:
  dataframe = query_BQ_table(query)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_vendor_offline_skam*: Failed to get data: ' + str(e)})

try:
  reponse_code_list, json_list = send_request_line_api_v6(url = url, headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_vendor_offline_skam*: Failed send API request: ' + str(e)})

dataframe1 = dataframe.filter(items=['vendor_code', 'line_user_id'])
dataframe1["return_response"] = reponse_code_list
dataframe1["msg_sent_date_time"] = now
dataframe1["template_id_if_any"] = "line_vendor_offline_skam"
dataframe1["msg_url"] = url
dataframe1["msg_content"] = 'content vendor_name: ' + dataframe['vendor_name'] \
                            +','+'content start_date_in_thai: ' + dataframe['start_date_in_thai'] \
                            +','+'content end_date_in_thai: ' + dataframe['end_date_in_thai'] \
                            +','+'content total_offline_hours: ' + dataframe['total_offline_hours']
df_records = dataframe1.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_vendor_offline_skam*: Failed to record logs: ' + str(e)})
