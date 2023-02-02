import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="a")
                    
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api
from get_secrete_token import get_secret_data
import datetime, pytz



# Basic configuration tables
query_table = "foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup"
verification_table = "fulfillment-dwh-production.pandata_report.country_TH_general_pd_vendors"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

# Basic configuration parameters
Live = True
url = "https://api.line.me/v2/bot/user/user_id_variable/richmenu/richmenu-55b2f4bf95dfb0c75d39f109075e4690"
json = {}
token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}"}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
    SELECT 
      line_data.VendorCode AS vendor_code,
      line_data.LineUserID AS line_user_id,
    FROM {query_table} AS line_data
    WHERE line_data.LineUserID IN ("U2b9495e231b925da2ed4163beeef6dad")
    QUALIFY ROW_NUMBER() OVER (
      PARTITION BY
      line_data.LineUserID,
      line_data.VendorCode
      ORDER BY
      line_data.Date DESC
    ) = 1
    ORDER BY line_data.Date
    """

if Live == True:
    query = f"""
    SELECT 
      vendor_data.vendor_code AS vendor_code,
      line_data.LineUserID AS line_user_id
    FROM {query_table} AS line_data
    INNER JOIN {verification_table} AS vendor_data
            ON lower(line_data.VendorCode) = lower(vendor_data.vendor_code)
    WHERE LineUserID IS NOT NULL
        AND VendorCode IS NOT NULL
        AND LOWER(VendorCode) NOT LIKE '%test%'
        AND vendor_data.is_active
        AND NOT vendor_data.is_private
        AND NOT vendor_data.is_test
     -- AND EXTRACT(DATE FROM Date) = CURRENT_DATE - 1
    QUALIFY ROW_NUMBER() OVER (
      PARTITION BY
      line_data.LineUserID,
      line_data.VendorCode
      ORDER BY
      line_data.Date DESC
    ) = 1
    ORDER BY line_data.Date
    """

try: 
  dataframe = query_BQ_table(query)
  user_id_list = dataframe["line_user_id"].tolist()
except BaseException as e:
    logging.info('Failed to get data: ' + str(e))

try:
  reponse_code_list, url_list = send_request_line_api(url, headers, json, user_id_list)
except BaseException as e:
    logging.info('Failed send API request: ' + str(e))

dataframe["return_response"] = reponse_code_list
dataframe["msg_sent_date_time"] = now
dataframe["template_id_if_any"] = "richmenu-55b2f4bf95dfb0c75d39f109075e4690"
dataframe["msg_url"] = url_list
dataframe["msg_content"] = "NA"
df_records = dataframe.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    logging.info('Failed to record logs: ' + str(e))

logging.info(status)