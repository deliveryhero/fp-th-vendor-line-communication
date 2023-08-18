import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_insight_basket_size
from get_secrete_token import get_secret_data
import datetime, pytz
import requests 
from template import json_object

# Basic configuration tables
query_table_vendor = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_insight_report_basket_size_vendor"
query_table_zone = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_insight_report_basket_size_zone"
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
    zone_base_data AS (
      SELECT 
        vendor_code,
        zone_name, 
        MAX(IF(range_gfv = "0-100 THB", perc_total_gfv, 0)) AS zone_0_100,
        MAX(IF(range_gfv = "101-200 THB", perc_total_gfv, 0)) AS zone_101_200,
        MAX(IF(range_gfv = "201-300 THB", perc_total_gfv, 0)) AS zone_201_300,
        MAX(IF(range_gfv = "301-400 THB", perc_total_gfv, 0)) AS zone_301_400,
        MAX(IF(range_gfv = ">401 THB", perc_total_gfv, 0)) AS zone_401
      FROM {query_table_zone}
      GROUP BY
      vendor_code,
      zone_name 
    ),
    zone_data AS (
      SELECT 
        vendor_code,
        zone_name,
        CAST(ROUND(zone_0_100*100,0) AS INT64) AS zone_0_100,
        CAST(ROUND(zone_101_200*100,0) AS INT64) AS zone_101_200,
        CAST(ROUND(zone_201_300*100,0) AS INT64) AS zone_201_300,
        CAST(ROUND(zone_301_400*100,0) AS INT64) AS zone_301_400,
        CAST(ROUND(zone_401*100,0) AS INT64) AS zone_401
      FROM zone_base_data
    ),
    vendor_base_data AS (
      SELECT 
        vendor_code,
        vendor_name_thai AS vendor_name,
        MAX(IF(range_gfv = "0-100 THB", perc, 0)) AS vendor_0_100,
        MAX(IF(range_gfv = "101-200 THB", perc, 0)) AS vendor_101_200,
        MAX(IF(range_gfv = "201-300 THB", perc, 0)) AS vendor_201_300,
        MAX(IF(range_gfv = "301-400 THB", perc, 0)) AS vendor_301_400,
        MAX(IF(range_gfv = ">401 THB", perc, 0)) AS vendor_401
      FROM {query_table_vendor}
      GROUP BY 
        vendor_code,
        vendor_name
    ),
    vendor_data AS (
      SELECT 
        vendor_code,
        vendor_name,
        CAST(ROUND(vendor_0_100*100,0) AS INT64) AS vendor_0_100,
        CAST(ROUND(vendor_101_200*100,0) AS INT64) AS vendor_101_200,
        CAST(ROUND(vendor_201_300*100,0) AS INT64) AS vendor_201_300,
        CAST(ROUND(vendor_301_400*100,0) AS INT64) AS vendor_301_400,
        CAST(ROUND(vendor_401*100,0) AS INT64) AS vendor_401
      FROM vendor_base_data
    )
    SELECT
      vendor_data.vendor_code,
      'U2b9495e231b925da2ed4163beeef6dad' AS line_user_id, 
      vendor_data.vendor_name,
      zone_data.zone_name,
      vendor_data.vendor_0_100,
      vendor_data.vendor_101_200,
      vendor_data.vendor_201_300,
      vendor_data.vendor_301_400,
      vendor_data.vendor_401,
      zone_data.zone_0_100,
      zone_data.zone_101_200,
      zone_data.zone_201_300,
      zone_data.zone_301_400,
      zone_data.zone_401
    FROM vendor_data
    INNER JOIN zone_data
            ON vendor_data.vendor_code = zone_data.vendor_code
    INNER JOIN line_data
            ON vendor_data.vendor_code = line_data.vendor_code
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
    zone_base_data AS (
      SELECT 
        vendor_code,
        zone_name, 
        MAX(IF(range_gfv = "0-100 THB", perc_total_gfv, 0)) AS zone_0_100,
        MAX(IF(range_gfv = "101-200 THB", perc_total_gfv, 0)) AS zone_101_200,
        MAX(IF(range_gfv = "201-300 THB", perc_total_gfv, 0)) AS zone_201_300,
        MAX(IF(range_gfv = "301-400 THB", perc_total_gfv, 0)) AS zone_301_400,
        MAX(IF(range_gfv = ">401 THB", perc_total_gfv, 0)) AS zone_401
      FROM {query_table_zone}
      GROUP BY
      vendor_code,
      zone_name 
    ),
    zone_data AS (
      SELECT 
        vendor_code,
        zone_name,
        CAST(ROUND(zone_0_100*100,0) AS INT64) AS zone_0_100,
        CAST(ROUND(zone_101_200*100,0) AS INT64) AS zone_101_200,
        CAST(ROUND(zone_201_300*100,0) AS INT64) AS zone_201_300,
        CAST(ROUND(zone_301_400*100,0) AS INT64) AS zone_301_400,
        CAST(ROUND(zone_401*100,0) AS INT64) AS zone_401
      FROM zone_base_data
    ),
    vendor_base_data AS (
      SELECT 
        vendor_code,
        vendor_name_thai AS vendor_name,
        MAX(IF(range_gfv = "0-100 THB", perc, 0)) AS vendor_0_100,
        MAX(IF(range_gfv = "101-200 THB", perc, 0)) AS vendor_101_200,
        MAX(IF(range_gfv = "201-300 THB", perc, 0)) AS vendor_201_300,
        MAX(IF(range_gfv = "301-400 THB", perc, 0)) AS vendor_301_400,
        MAX(IF(range_gfv = ">401 THB", perc, 0)) AS vendor_401
      FROM {query_table_vendor}
      GROUP BY 
        vendor_code,
        vendor_name
    ),
    vendor_data AS (
      SELECT 
        vendor_code,
        vendor_name,
        CAST(ROUND(vendor_0_100*100,0) AS INT64) AS vendor_0_100,
        CAST(ROUND(vendor_101_200*100,0) AS INT64) AS vendor_101_200,
        CAST(ROUND(vendor_201_300*100,0) AS INT64) AS vendor_201_300,
        CAST(ROUND(vendor_301_400*100,0) AS INT64) AS vendor_301_400,
        CAST(ROUND(vendor_401*100,0) AS INT64) AS vendor_401
      FROM vendor_base_data
    )
    SELECT
      vendor_data.vendor_code,
      line_data.line_user_id,
      vendor_data.vendor_name,
      zone_data.zone_name,
      vendor_data.vendor_0_100,
      vendor_data.vendor_101_200,
      vendor_data.vendor_201_300,
      vendor_data.vendor_301_400,
      vendor_data.vendor_401,
      zone_data.zone_0_100,
      zone_data.zone_101_200,
      zone_data.zone_201_300,
      zone_data.zone_301_400,
      zone_data.zone_401
    FROM vendor_data
    INNER JOIN zone_data
            ON vendor_data.vendor_code = zone_data.vendor_code
    INNER JOIN line_data
            ON vendor_data.vendor_code = line_data.vendor_code
    """

try: 
  dataframe = query_BQ_table(query)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_basket_size*: Failed to get data: ' + str(e)})

try:
  reponse_code_list, json_list = send_request_line_api_insight_basket_size(url = url, headers = headers, 
                                                          json_object = json_object, 
                                                          dataframe = dataframe)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_basket_size*: Failed send API request: ' + str(e)})

dataframe1 = dataframe.filter(items=['vendor_code', 'line_user_id'])
dataframe1["return_response"] = reponse_code_list
dataframe1["msg_sent_date_time"] = now
dataframe1["template_id_if_any"] = "line_insight_report_basket_size"
dataframe1["msg_url"] = url
dataframe1["msg_content"] = json_list
df_records = dataframe1.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_basket_size*: Failed to record logs: ' + str(e)})
