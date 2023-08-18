import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_insight_top_3_and_ractors
from get_secrete_token import get_secret_data
import datetime, pytz
import requests 
from template import json_object

# Basic configuration tables
query_table_top_3_vendors = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_insight_report_top_3_and_factors_top3"
query_table_vendor = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_insight_report_top_3_and_factors_vendor"
query_table_zone = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_insight_report_top_3_and_factors_zone"
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
    top_vendor AS (
      SELECT 
      vendor_code,
      MAX(IF(row_num = 1, top_vendor_name, NULL)) AS top_vendor_name_1,
      MAX(IF(row_num = 2, top_vendor_name, NULL)) AS top_vendor_name_2,
      MAX(IF(row_num = 3, top_vendor_name, NULL)) AS top_vendor_name_3,
      FROM {query_table_top_3_vendors}
      GROUP BY vendor_code
    ),
    zone_data AS (
    SELECT  
      zone.vendor_code,
      zone.vendor_name_thai	AS vendor_name,
      zone.cuisine_type,
      zone.zone_name,
      CAST(ROUND(zone.perc_dld*100,0) AS INT64) AS zone_perc_dld,
      CAST(ROUND(zone.perc_dlp*100,0) AS INT64) AS zone_perc_dlp,
      CAST(ROUND(zone.perc_failed_rate*100,0) AS INT64) AS zone_perc_failed_rate,
      CAST(ROUND(zone.off_pct*100,0) AS INT64) AS zone_off_pct,
      zone.rating AS zone_rating
    FROM {query_table_zone} AS zone
    ),
    vendor_data AS (
      SELECT  
        vendor.vendor_code,
        vendor.vendor_name,
        vendor.cuisine_type,
        CAST(ROUND(vendor.perc_dld*100,0) AS INT64) AS vendor_perc_dld,
        CAST(ROUND(vendor.perc_dlp*100,0) AS INT64) AS vendor_perc_dlp,
        CAST(ROUND(vendor.perc_failed_rate*100,0) AS INT64) AS vendor_perc_failed_rate,
        CAST(ROUND(vendor.off_pct*100,0) AS INT64) AS vendor_off_pct,
        vendor.rating AS vendor_rating
      FROM {query_table_vendor} AS vendor
    )
    SELECT
      zone_data.vendor_code,
      'U2b9495e231b925da2ed4163beeef6dad' AS line_user_id, 
      zone_data.vendor_name,
      zone_data.cuisine_type,
      zone_data.zone_name,
      IFNULL(top_vendor.top_vendor_name_1,"NA") AS top_vendor_name_1,
      IFNULL(top_vendor.top_vendor_name_2,"NA") AS top_vendor_name_2,
      IFNULL(top_vendor.top_vendor_name_3,"NA") AS top_vendor_name_3,
      IFNULL(zone_data.zone_perc_dld,0) AS zone_perc_dld,
      IFNULL(zone_data.zone_perc_dlp,0) AS zone_perc_dlp,
      IFNULL(zone_data.zone_perc_failed_rate,0) AS zone_perc_failed_rate,
      IFNULL(zone_data.zone_off_pct,0) AS zone_off_pct,
      IFNULL(zone_data.zone_rating,0) AS zone_rating,
      IFNULL(vendor_data.vendor_perc_dld,0) AS vendor_perc_dld,
      IFNULL(vendor_data.vendor_perc_dlp,0) AS vendor_perc_dlp,
      IFNULL(vendor_data.vendor_perc_failed_rate,0) AS vendor_perc_failed_rate,
      IFNULL(vendor_data.vendor_off_pct,0) AS vendor_off_pct,
      IFNULL(vendor_data.vendor_rating,0) AS vendor_rating
    FROM zone_data
    INNER JOIN vendor_data
            ON zone_data.vendor_code = vendor_data.vendor_code
    INNER JOIN top_vendor
            ON vendor_data.vendor_code = top_vendor.vendor_code
    INNER JOIN line_data
            ON zone_data.vendor_code = line_data.vendor_code
    QUALIFY ROW_NUMBER() OVER (PARTITION BY zone_data.vendor_code) = 1
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
    top_vendor AS (
      SELECT 
      vendor_code,
      MAX(IF(row_num = 1, top_vendor_name, NULL)) AS top_vendor_name_1,
      MAX(IF(row_num = 2, top_vendor_name, NULL)) AS top_vendor_name_2,
      MAX(IF(row_num = 3, top_vendor_name, NULL)) AS top_vendor_name_3,
      FROM {query_table_top_3_vendors}
      GROUP BY vendor_code
    ),
    zone_data AS (
    SELECT  
      zone.vendor_code,
      zone.vendor_name_thai	AS vendor_name,
      zone.cuisine_type,
      zone.zone_name,
      CAST(ROUND(zone.perc_dld*100,0) AS INT64) AS zone_perc_dld,
      CAST(ROUND(zone.perc_dlp*100,0) AS INT64) AS zone_perc_dlp,
      CAST(ROUND(zone.perc_failed_rate*100,0) AS INT64) AS zone_perc_failed_rate,
      CAST(ROUND(zone.off_pct*100,0) AS INT64) AS zone_off_pct,
      zone.rating AS zone_rating
    FROM {query_table_zone} AS zone
    ),
    vendor_data AS (
      SELECT  
        vendor.vendor_code,
        vendor.vendor_name,
        vendor.cuisine_type,
        CAST(ROUND(vendor.perc_dld*100,0) AS INT64) AS vendor_perc_dld,
        CAST(ROUND(vendor.perc_dlp*100,0) AS INT64) AS vendor_perc_dlp,
        CAST(ROUND(vendor.perc_failed_rate*100,0) AS INT64) AS vendor_perc_failed_rate,
        CAST(ROUND(vendor.off_pct*100,0) AS INT64) AS vendor_off_pct,
        vendor.rating AS vendor_rating
      FROM {query_table_vendor} AS vendor
    )
    SELECT
      zone_data.vendor_code,
      line_data.line_user_id,
      zone_data.vendor_name,
      zone_data.cuisine_type,
      zone_data.zone_name,
      IFNULL(top_vendor.top_vendor_name_1,"NA") AS top_vendor_name_1,
      IFNULL(top_vendor.top_vendor_name_2,"NA") AS top_vendor_name_2,
      IFNULL(top_vendor.top_vendor_name_3,"NA") AS top_vendor_name_3,
      IFNULL(zone_data.zone_perc_dld,0) AS zone_perc_dld,
      IFNULL(zone_data.zone_perc_dlp,0) AS zone_perc_dlp,
      IFNULL(zone_data.zone_perc_failed_rate,0) AS zone_perc_failed_rate,
      IFNULL(zone_data.zone_off_pct,0) AS zone_off_pct,
      IFNULL(zone_data.zone_rating,0) AS zone_rating,
      IFNULL(vendor_data.vendor_perc_dld,0) AS vendor_perc_dld,
      IFNULL(vendor_data.vendor_perc_dlp,0) AS vendor_perc_dlp,
      IFNULL(vendor_data.vendor_perc_failed_rate,0) AS vendor_perc_failed_rate,
      IFNULL(vendor_data.vendor_off_pct,0) AS vendor_off_pct,
      IFNULL(vendor_data.vendor_rating,0) AS vendor_rating
    FROM zone_data
    INNER JOIN vendor_data
            ON zone_data.vendor_code = vendor_data.vendor_code
    INNER JOIN top_vendor
            ON vendor_data.vendor_code = top_vendor.vendor_code
    INNER JOIN line_data
            ON zone_data.vendor_code = line_data.vendor_code
    QUALIFY ROW_NUMBER() OVER (PARTITION BY zone_data.vendor_code) = 1
    """

try: 
  dataframe = query_BQ_table(query)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_top_3_and_ractors*: Failed to get data: ' + str(e)})

try:
  reponse_code_list, json_list = send_request_line_api_insight_top_3_and_ractors(url = url, headers = headers, 
                                                          json_object = json_object, 
                                                          dataframe = dataframe)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_top_3_and_ractors*: Failed send API request: ' + str(e)})

dataframe1 = dataframe.filter(items=['vendor_code', 'line_user_id'])
dataframe1["return_response"] = reponse_code_list
dataframe1["msg_sent_date_time"] = now
dataframe1["template_id_if_any"] = "line_insight_report_top_3_and_ractors"
dataframe1["msg_url"] = url
dataframe1["msg_content"] = json_list
df_records = dataframe1.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_insight_report_top_3_and_ractors*: Failed to record logs: ' + str(e)})
