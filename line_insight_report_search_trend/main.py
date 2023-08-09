import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_insight_search_term
from get_secrete_token import get_secret_data
import datetime, pytz
import requests 
from template import json_object

# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_insight_report_search_trend"
line_data  = "foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup"
pii_data = "foodpanda-th-bigquery.pandata_th.sf_account_internal_non_pii"
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
      WITH line_base_data AS (
        SELECT
          VendorCode,
          LineUserID,
          IF(
              LENGTH(VendorMobile) = 9,
              CONCAT("+66", VendorMobile),
              REGEXP_REPLACE(TRIM(LOWER(REPLACE(VendorMobile, "-", ""))), r"^0+", "+66")
          ) AS vendor_mobile,
        FROM {line_data}
        WHERE (Owner IS NOT NULL OR Manager IS NOT NULL)
          AND LineUserID IS NOT NULL
      ),
      line_data AS (
      SELECT
        line_base_data.VendorCode AS vendor_code,
        line_base_data.LineUserID AS line_user_id,
      FROM line_base_data
      INNER JOIN {pii_data} AS pii_data
              ON pii_data.vendor_code = line_base_data.VendorCode
            AND pii_data.account_phone = line_base_data.vendor_mobile
      ),
      search_data AS (
        SELECT 
          vendor_code,
          vendor_name, 
          zone_name,
          MAX(IF(row_num = 1, search_term, NULL)) AS serch_term_1,
          MAX(IF(row_num = 2, search_term, NULL)) AS serch_term_2,
          MAX(IF(row_num = 3, search_term, NULL)) AS serch_term_3,
          MAX(IF(row_num = 4, search_term, NULL)) AS serch_term_4,
          MAX(IF(row_num = 5, search_term, NULL)) AS serch_term_5
        FROM {query_table}
        GROUP BY 
          vendor_code,
          vendor_name,
          zone_name
      )
      SELECT
        search_data.vendor_code,
        'U2b9495e231b925da2ed4163beeef6dad' AS line_user_id, 
        search_data.vendor_name,
        search_data.zone_name,
        search_data.serch_term_1,
        search_data.serch_term_2,
        search_data.serch_term_3,
        search_data.serch_term_4,
        search_data.serch_term_5
      FROM search_data
      INNER JOIN line_data
              ON search_data.vendor_code = line_data.vendor_code
    LIMIT 1
    """

if Live == True:
    query = f"""
    WITH line_base_data AS (
      SELECT
        VendorCode,
        LineUserID,
        IF(
            LENGTH(VendorMobile) = 9,
            CONCAT("+66", VendorMobile),
            REGEXP_REPLACE(TRIM(LOWER(REPLACE(VendorMobile, "-", ""))), r"^0+", "+66")
        ) AS vendor_mobile,
      FROM {line_data}
      WHERE (Owner IS NOT NULL OR Manager IS NOT NULL)
        AND LineUserID IS NOT NULL
    ),
    line_data AS (
    SELECT
      line_base_data.VendorCode AS vendor_code,
      line_base_data.LineUserID AS line_user_id,
    FROM line_base_data
    INNER JOIN {pii_data} AS pii_data
            ON pii_data.vendor_code = line_base_data.VendorCode
          AND pii_data.account_phone = line_base_data.vendor_mobile
    ),
    search_data AS (
      SELECT 
        vendor_code,
        vendor_name, 
        zone_name,
        MAX(IF(row_num = 1, search_term, NULL)) AS serch_term_1,
        MAX(IF(row_num = 2, search_term, NULL)) AS serch_term_2,
        MAX(IF(row_num = 3, search_term, NULL)) AS serch_term_3,
        MAX(IF(row_num = 4, search_term, NULL)) AS serch_term_4,
        MAX(IF(row_num = 5, search_term, NULL)) AS serch_term_5
      FROM {query_table}
      GROUP BY 
        vendor_code,
        vendor_name,
        zone_name
    )
    SELECT
      search_data.vendor_code,
      line_data.line_user_id,
      search_data.vendor_name,
      search_data.zone_name,
      search_data.serch_term_1,
      search_data.serch_term_2,
      search_data.serch_term_3,
      search_data.serch_term_4,
      search_data.serch_term_5
    FROM search_data
    INNER JOIN line_data
            ON search_data.vendor_code = line_data.vendor_code
    """

try: 
  dataframe = query_BQ_table(query)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_search_trend*: Failed to get data: ' + str(e)})

try:
  reponse_code_list, json_list = send_request_line_api_insight_search_term(url = url, headers = headers, 
                                                          json_object = json_object, 
                                                          dataframe = dataframe)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_search_trend*: Failed send API request: ' + str(e)})

dataframe1 = dataframe.filter(items=['vendor_code', 'line_user_id'])
dataframe1["return_response"] = reponse_code_list
dataframe1["msg_sent_date_time"] = now
dataframe1["template_id_if_any"] = "line_insight_report_search_trend"
dataframe1["msg_url"] = url
dataframe1["msg_content"] = json_list
df_records = dataframe1.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_search_trend*: Failed to record logs: ' + str(e)})
