import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_insight_opening_time
from get_secrete_token import get_secret_data
import datetime, pytz
import requests 
from template import json_object

# Basic configuration tables
query_table_vendor = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_insight_report_opening_time_vendor"
query_table_zone = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_insight_report_opening_time_zone"
line_data  = "foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup"
pii_data = "foodpanda-th-bigquery.pandata_th.sf_account_internal_non_pii"
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
        MAX(IF(periods = "5AM  - 10AM (มื้อเช้า)", perc_total_orders, 0)) AS zone_5AM_10AM,
        MAX(IF(periods = "10AM  - 2PM (มื้อกลางวัน)", perc_total_orders, 0)) AS zone_10AM_2PM,
        MAX(IF(periods = "2PM  - 5PM (มื้อบ่าย)", perc_total_orders, 0)) AS zone_2PM_5PM,
        MAX(IF(periods = "5PM  - 10PM (มื้อเย็น)", perc_total_orders, 0)) AS zone_5PM_10PM,
        MAX(IF(periods = "10PM - 5AM (มื้อดึก)", perc_total_orders, 0)) AS zone_10PM_5AM
      FROM {query_table_zone}
      GROUP BY 
        vendor_code,
        zone_name
    ),
    zone_data AS (
      SELECT 
        vendor_code,
        zone_name,
        CAST(ROUND(zone_5AM_10AM*100,0) AS INT64) AS zone_5AM_10AM,
        CAST(ROUND(zone_10AM_2PM*100,0) AS INT64) AS zone_10AM_2PM,
        CAST(ROUND(zone_2PM_5PM*100,0) AS INT64) AS zone_2PM_5PM,
        CAST(ROUND(zone_5PM_10PM*100,0) AS INT64) AS zone_5PM_10PM,
        CAST(ROUND(zone_10PM_5AM*100,0) AS INT64) AS zone_10PM_5AM
      FROM zone_base_data
    ),
    vendor_base_data AS (
      SELECT
        vendor_code,
        vendor_name_thai AS vendor_name,
        MAX(IF(periods = "5AM  - 10AM (มื้อเช้า)", perc, 0)) AS vendor_5AM_10AM,
        MAX(IF(periods = "10AM  - 2PM (มื้อกลางวัน)", perc, 0)) AS vendor_10AM_2PM,
        MAX(IF(periods = "2PM  - 5PM (มื้อบ่าย)", perc, 0)) AS vendor_2PM_5PM,
        MAX(IF(periods = "5PM  - 10PM (มื้อเย็น)", perc, 0)) AS vendor_5PM_10PM,
        MAX(IF(periods = "10PM - 5AM (มื้อดึก)", perc, 0)) AS vendor_10PM_5AM
      FROM {query_table_vendor}
      GROUP BY 
        vendor_code,
        vendor_name 
    ),
    vendor_data AS (
      SELECT 
        vendor_code,
        vendor_name,
        CAST(ROUND(vendor_5AM_10AM*100,0) AS INT64) AS vendor_5AM_10AM,
        CAST(ROUND(vendor_10AM_2PM*100,0) AS INT64) AS vendor_10AM_2PM,
        CAST(ROUND(vendor_2PM_5PM*100,0) AS INT64) AS vendor_2PM_5PM,
        CAST(ROUND(vendor_5PM_10PM*100,0) AS INT64) AS vendor_5PM_10PM,
        CAST(ROUND(vendor_10PM_5AM*100,0) AS INT64) AS vendor_10PM_5AM
      FROM vendor_base_data
    )
    SELECT
      vendor_data.vendor_code,
      'U2b9495e231b925da2ed4163beeef6dad' AS line_user_id, 
      vendor_data.vendor_name,
      zone_data.zone_name,
      zone_data.zone_5AM_10AM*3 AS zone_5AM_10AM,
      zone_data.zone_10AM_2PM*3 AS zone_10AM_2PM,
      zone_data.zone_2PM_5PM*3 AS zone_2PM_5PM,
      zone_data.zone_5PM_10PM*3 AS zone_5PM_10PM,
      zone_data.zone_10PM_5AM*3 AS zone_10PM_5AM,
      vendor_data.vendor_5AM_10AM*3 AS vendor_5AM_10AM,
      vendor_data.vendor_10AM_2PM*3 AS vendor_10AM_2PM,
      vendor_data.vendor_2PM_5PM*3 AS vendor_2PM_5PM,
      vendor_data.vendor_5PM_10PM*3 AS vendor_5PM_10PM,
      vendor_data.vendor_10PM_5AM*3 AS vendor_10PM_5AM
    FROM zone_data
    INNER JOIN vendor_data
            ON zone_data.vendor_code = vendor_data.vendor_code 
    INNER JOIN line_data
            ON zone_data.vendor_code = line_data.vendor_code
    QUALIFY ROW_NUMBER() OVER (PARTITION BY vendor_data.vendor_code, line_data.line_user_id) = 1
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
        MAX(IF(periods = "5AM  - 10AM (มื้อเช้า)", perc_total_orders, 0)) AS zone_5AM_10AM,
        MAX(IF(periods = "10AM  - 2PM (มื้อกลางวัน)", perc_total_orders, 0)) AS zone_10AM_2PM,
        MAX(IF(periods = "2PM  - 5PM (มื้อบ่าย)", perc_total_orders, 0)) AS zone_2PM_5PM,
        MAX(IF(periods = "5PM  - 10PM (มื้อเย็น)", perc_total_orders, 0)) AS zone_5PM_10PM,
        MAX(IF(periods = "10PM - 5AM (มื้อดึก)", perc_total_orders, 0)) AS zone_10PM_5AM
      FROM {query_table_zone}
      GROUP BY 
        vendor_code,
        zone_name
    ),
    zone_data AS (
      SELECT 
        vendor_code,
        zone_name,
        CAST(ROUND(zone_5AM_10AM*100,0) AS INT64) AS zone_5AM_10AM,
        CAST(ROUND(zone_10AM_2PM*100,0) AS INT64) AS zone_10AM_2PM,
        CAST(ROUND(zone_2PM_5PM*100,0) AS INT64) AS zone_2PM_5PM,
        CAST(ROUND(zone_5PM_10PM*100,0) AS INT64) AS zone_5PM_10PM,
        CAST(ROUND(zone_10PM_5AM*100,0) AS INT64) AS zone_10PM_5AM
      FROM zone_base_data
    ),
    vendor_base_data AS (
      SELECT
        vendor_code,
        vendor_name_thai AS vendor_name,
        MAX(IF(periods = "5AM  - 10AM (มื้อเช้า)", perc, 0)) AS vendor_5AM_10AM,
        MAX(IF(periods = "10AM  - 2PM (มื้อกลางวัน)", perc, 0)) AS vendor_10AM_2PM,
        MAX(IF(periods = "2PM  - 5PM (มื้อบ่าย)", perc, 0)) AS vendor_2PM_5PM,
        MAX(IF(periods = "5PM  - 10PM (มื้อเย็น)", perc, 0)) AS vendor_5PM_10PM,
        MAX(IF(periods = "10PM - 5AM (มื้อดึก)", perc, 0)) AS vendor_10PM_5AM
      FROM {query_table_vendor}
      GROUP BY 
        vendor_code,
        vendor_name 
    ),
    vendor_data AS (
      SELECT 
        vendor_code,
        vendor_name,
        CAST(ROUND(vendor_5AM_10AM*100,0) AS INT64) AS vendor_5AM_10AM,
        CAST(ROUND(vendor_10AM_2PM*100,0) AS INT64) AS vendor_10AM_2PM,
        CAST(ROUND(vendor_2PM_5PM*100,0) AS INT64) AS vendor_2PM_5PM,
        CAST(ROUND(vendor_5PM_10PM*100,0) AS INT64) AS vendor_5PM_10PM,
        CAST(ROUND(vendor_10PM_5AM*100,0) AS INT64) AS vendor_10PM_5AM
      FROM vendor_base_data
    )
    SELECT
      vendor_data.vendor_code,
      line_data.line_user_id,
      vendor_data.vendor_name,
      zone_data.zone_name,
      zone_data.zone_5AM_10AM*3 AS zone_5AM_10AM,
      zone_data.zone_10AM_2PM*3 AS zone_10AM_2PM,
      zone_data.zone_2PM_5PM*3 AS zone_2PM_5PM,
      zone_data.zone_5PM_10PM*3 AS zone_5PM_10PM,
      zone_data.zone_10PM_5AM*3 AS zone_10PM_5AM,
      vendor_data.vendor_5AM_10AM*3 AS vendor_5AM_10AM,
      vendor_data.vendor_10AM_2PM*3 AS vendor_10AM_2PM,
      vendor_data.vendor_2PM_5PM*3 AS vendor_2PM_5PM,
      vendor_data.vendor_5PM_10PM*3 AS vendor_5PM_10PM,
      vendor_data.vendor_10PM_5AM*3 AS vendor_10PM_5AM
    FROM zone_data
    INNER JOIN vendor_data
            ON zone_data.vendor_code = vendor_data.vendor_code 
    INNER JOIN line_data
            ON zone_data.vendor_code = line_data.vendor_code
    QUALIFY ROW_NUMBER() OVER (PARTITION BY vendor_data.vendor_code, line_data.line_user_id) = 1
    """

try: 
  dataframe = query_BQ_table(query)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_opening_time*: Failed to get data: ' + str(e)})

try:
  reponse_code_list, json_list = send_request_line_api_insight_opening_time(url = url, headers = headers, 
                                                          json_object = json_object, 
                                                          dataframe = dataframe)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_opening_time*: Failed send API request: ' + str(e)})

try:
  dataframe1 = dataframe.filter(items=['vendor_code', 'line_user_id'])
  dataframe1["return_response"] = reponse_code_list
  dataframe1["msg_sent_date_time"] = now
  dataframe1["template_id_if_any"] = "line_insight_report_opening_time"
  dataframe1["msg_url"] = url
  dataframe1["msg_content"] = json_list
  df_records = dataframe1.to_dict('records')
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_opening_time*: Failed to record logs: ' + str(e)})


