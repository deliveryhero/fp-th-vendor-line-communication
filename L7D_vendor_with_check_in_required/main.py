import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="a")
                    
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_v4
from get_secrete_token import get_secret_data
import datetime, pytz
import requests 
from template import json_object

# Basic configuration tables
query_table = "foodpanda-th-bigquery.pandata_th.L7D_vendor_with_check_in_required"
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
      'U2b9495e231b925da2ed4163beeef6dad' AS line_user_id, 
      sum_check_in_required_mins
    FROM {query_table}
    WHERE line_user_id IS NOT NULL
    LIMIT 1
    """

if Live == True:
    query = f"""
    SELECT DISTINCT 
      vendor_code, 
      line_user_id,  
      sum_check_in_required_mins
    FROM {query_table}
    WHERE line_user_id IS NOT NULL
    """

try: 
  dataframe = query_BQ_table(query)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*L7D_vendor_with_check_in_required*: Failed to get data: ' + str(e)})
    logging.info('Failed to get data: ' + str(e))

try:
  reponse_code_list, json_list = send_request_line_api_v4(url = url, headers = headers, 
                                                          json_object = json_object, 
                                                          dataframe = dataframe)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*L7D_vendor_with_check_in_required*: Failed send API request: ' + str(e)})
    logging.info('Failed send API request: ' + str(e))

dataframe = dataframe.filter(items=['vendor_code', 'line_user_id'])
dataframe["return_response"] = reponse_code_list
dataframe["msg_sent_date_time"] = now
dataframe["template_id_if_any"] = "L7D_vendor_with_check_in_required"
dataframe["msg_url"] = url
dataframe["msg_content"] = json_list
df_records = dataframe.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*L7D_vendor_with_check_in_required*: Failed to record logs: ' + str(e)})
    logging.info('Failed to record logs: ' + str(e))

logging.info(status)