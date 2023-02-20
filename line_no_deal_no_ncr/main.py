import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="a")

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api, send_request_line_api_v2
from get_secrete_token import get_secret_data
import datetime, pytz


# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_auto_sms_no_deal_no_ncr"
# line_data  = "foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

# Basic configuration parameters
Live = False
url = "https://api.line.me/v2/bot/message/push"
json_data = {
    "to": "{{custom_attribute.${lineuserid}}}",
    "messages": [
        {
            "type": "flex",
            "altText": "ยังไม่ได้ออเดอร์? ไม่ต้องกังวัล!",
            "contents":
{
  "type": "bubble",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "vertical",
    "position": "relative",
    "backgroundColor": "#F7C6CCFF",
    "borderColor": "#F7C6CC",
    "contents": [
      {
        "type": "image",
        "url": "https://drive.google.com/uc?export=view&id=1fJvo02AE5IbbpoCleazXRb29ww0cQe-7",
        "align": "center",
        "gravity": "center",
        "size": "full",
        "aspectMode": "fit",
        "action": {
          "type": "uri",
          "label": "คลิก!",
          "uri": "https://foodpanda.portal.restaurant/promotion?int_ref=side-nav"
        }
      }
    ]
  }
}
    }
  ]
}


json_string = str(json_data)

token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}", 'Content-Type': 'application/json'}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
    SELECT
        vendor_data.vendor_code AS vendor_code,
        'U2b9495e231b925da2ed4163beeef6dad' AS line_user_id,
    FROM {query_table} AS vendor_data
    WHERE is_line_verified
    LIMIT 1
    """

if Live == True:
    query = f"""
    SELECT DISTINCT
        vendor_data.vendor_code AS vendor_code,
        vendor_data.line_user_id,
    FROM {query_table} AS vendor_data
    WHERE is_line_verified
    """

try:
  dataframe = query_BQ_table(query)
  user_id_list = dataframe["line_user_id"].tolist()
except BaseException as e:
    logging.info('Failed to get data: ' + str(e))

try:
  reponse_code_list, json_list = send_request_line_api_v2(url, headers, json_data, user_id_list)
except BaseException as e:
    logging.info('Failed send API request: ' + str(e))

dataframe["return_response"] = reponse_code_list
dataframe["msg_sent_date_time"] = now
dataframe["template_id_if_any"] = "line_no_deal_no_snr"
dataframe["msg_url"] = url
dataframe["msg_content"] = json_list
df_records = dataframe.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    logging.info('Failed to record logs: ' + str(e))

logging.info(status)