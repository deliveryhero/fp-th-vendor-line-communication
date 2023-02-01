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
import datetime


# Basic configuration tables
query_table = "foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup"
verification_table = "fulfillment-dwh-production.pandata_report.country_TH_general_pd_vendors"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs"

# Basic configuration parameters
Live = False
url = "https://api.line.me/v2/bot/user/user_id_variable/richmenu/richmenu-55b2f4bf95dfb0c75d39f109075e4690"
json = {}
token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}"}
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
    SELECT 
      line_data.VendorCode AS vendor_code,
      line_data.LineUserID AS line_user_id,
    FROM {query_table} AS line_data
    WHERE line_data.LineUserID IN ("U5f25d7890e933d09ef30f8bcf98b8043")
    ORDER BY Date
    """

if Live == True:
    query = f"""
    SELECT 
      line_data.VendorCode,
      line_data.LineUserID
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
    ORDER BY Date
    """


dataframe = query_BQ_table(query)
print(dataframe)
user_id_list = dataframe["line_user_id"].tolist()

reponse_code_list, url_list = send_request_line_api(url, headers, json, user_id_list)
dataframe["return_response"] = reponse_code_list
dataframe["msg_sent_date_time"] = now
dataframe["template_id_if_any"] = "richmenu-55b2f4bf95dfb0c75d39f109075e4690"
dataframe["msg_url"] = url_list
dataframe["msg_content"] = "NA"
df_records = dataframe.to_dict('records')

status = record_line_communication_logs(logs_table_id, df_records)

logging.info(status)