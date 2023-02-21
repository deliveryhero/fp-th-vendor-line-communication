import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="a")
                    
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_v3
from get_secrete_token import get_secret_data
import datetime, pytz
from template import json_object
import requests 


# Basic configuration tables
query_table = "foodpanda-th-bigquery.pandata_th.incubation_weekly_report_line_communication"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

# Basic configuration parameters
Live = True
url = "https://api.line.me/v2/bot/message/push"
json_data = json_object
token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}", 'Content-Type': 'application/json'}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
    SELECT * EXCEPT (LineUserID),
    'U2b9495e231b925da2ed4163beeef6dad' AS LineUserID
    FROM {query_table}
    WHERE vendor_code != 'a0j1'
    LIMIT 1 
    """

if Live == True:
    query = f"""
    SELECT * FROM {query_table} 
    WHERE vendor_code IS NOT NULL
    AND LineUserID IS NOT NULL
    """

try: 
  dataframe = query_BQ_table(query)
except BaseException as e:
    requests.post('https://hooks.slack.com/services/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',
    json = {'text' : '*Incubation_weekly_report*: Failed to get data: ' + str(e)})
    logging.info('Failed to get data: ' + str(e))

try:
  reponse_code_list, json_list = send_request_line_api_v3(url = url, headers = headers, 
                                                          json_object = json_object, 
                                                          dataframe = dataframe)
except BaseException as e:
    requests.post('https://hooks.slack.com/services/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',
    json = {'text' : '*Incubation_weekly_report*: Failed send API request: ' + str(e)})
    logging.info('Failed send API request: ' + str(e))

dataframe = dataframe.filter(items=['vendor_code', 'LineUserID'])
dataframe.rename(columns={'LineUserID': 'line_user_id'}, inplace=True)
dataframe["return_response"] = reponse_code_list
dataframe["msg_sent_date_time"] = now
dataframe["template_id_if_any"] = "Incubation_weekly_report"
dataframe["msg_url"] = url
dataframe["msg_content"] = json_list
df_records = dataframe.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post('https://hooks.slack.com/services/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',
    json = {'text' : '*Incubation_weekly_report*: Failed to record logs: ' + str(e)})
    logging.info('Failed to record logs: ' + str(e))

logging.info(status)