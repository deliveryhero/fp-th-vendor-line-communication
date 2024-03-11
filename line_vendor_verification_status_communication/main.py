import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_line_vendor_verification_status_communication
from get_secrete_token import get_secret_data
import datetime, pytz
import requests
from template import json_object_success, json_object_not_success

# Basic configuration tables
line_data  = "foodpanda-th-bigquery.pandata_th_external.vendor_experience_line_liff_user_data"
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
    WITH base_data AS (
      SELECT 
        VendorCode,
        LineUserID,
        VendorMobile
      FROM `foodpanda-th-bigquery.pandata_th_external.vendor_experience_line_liff_user_data` 
      WHERE Date IS NOT NULL
        AND Date > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 2 HOUR)
        AND VendorCode IS NOT NULL
        AND VendorMobile IS NOT NULL
        AND LineUserID IS NOT NULL
    ),

    processed_data AS (
      SELECT
        COALESCE(pii_data.vendor_code, base_data.VendorCode) AS vendor_code, 
        base_data.LineUserID AS line_user_id,
        CASE 
          WHEN pii_data.vendor_code IS NULL
            THEN "NotSuccessfulVerification"
            ELSE "SuccessfulVerification"
          END as verfication_status
      FROM base_data
      LEFT JOIN `foodpanda-th-bigquery.pandata_th.sf_account_internal_non_pii` AS pii_data
            ON LOWER(base_data.VendorCode) = LOWER(pii_data.vendor_code)
            AND pii_data.account_phone = IF(LENGTH(base_data.VendorMobile) = 9,
                                                  CONCAT("+66", base_data.VendorMobile),
                                                  REGEXP_REPLACE(TRIM(LOWER(REPLACE(base_data.VendorMobile, "-", ""))), r"^0+", "+66"))
      QUALIFY ROW_NUMBER() OVER(PARTITION BY base_data.VendorCode, base_data.LineUserID) = 1
    )

    SELECT
      processed_data.vendor_code,
      processed_data.line_user_id,
      processed_data.verfication_status
    FROM processed_data
    LEFT JOIN `foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live` AS logs
          ON processed_data.vendor_code = logs.vendor_code
          AND processed_data.line_user_id = logs.line_user_id
          AND processed_data.verfication_status = logs.msg_content
    WHERE logs.vendor_code IS NULL
      AND processed_data.line_user_id IN ("U9d1f00f6f00199356eee821cb2736ac2", "U0276f51ba4f3f5f0e275ebcdbbc11b6d","U5f25d7890e933d09ef30f8bcf98b8043","U2b9495e231b925da2ed4163beeef6dad", "U592e83eced3872c667f8dbe4e7277b8a")
    """

if Live == True:
    query = f"""
    WITH base_data AS (
      SELECT 
        VendorCode,
        LineUserID,
        VendorMobile
      FROM `foodpanda-th-bigquery.pandata_th_external.vendor_experience_line_liff_user_data` 
      WHERE Date IS NOT NULL
        AND Date > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 2 HOUR)
        AND VendorCode IS NOT NULL
        AND VendorMobile IS NOT NULL
        AND LineUserID IS NOT NULL
    ),

    processed_data AS (
      SELECT
        COALESCE(pii_data.vendor_code, base_data.VendorCode) AS vendor_code, 
        base_data.LineUserID AS line_user_id,
        CASE 
          WHEN pii_data.vendor_code IS NULL
            THEN "NotSuccessfulVerification"
            ELSE "SuccessfulVerification"
          END as verfication_status
      FROM base_data
      LEFT JOIN `foodpanda-th-bigquery.pandata_th.sf_account_internal_non_pii` AS pii_data
            ON LOWER(base_data.VendorCode) = LOWER(pii_data.vendor_code)
            AND pii_data.account_phone = IF(LENGTH(base_data.VendorMobile) = 9,
                                                  CONCAT("+66", base_data.VendorMobile),
                                                  REGEXP_REPLACE(TRIM(LOWER(REPLACE(base_data.VendorMobile, "-", ""))), r"^0+", "+66"))
      QUALIFY ROW_NUMBER() OVER(PARTITION BY base_data.VendorCode, base_data.LineUserID) = 1
    )

    SELECT
      processed_data.vendor_code,
      processed_data.line_user_id,
      processed_data.verfication_status
    FROM processed_data
    LEFT JOIN `foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live` AS logs
          ON processed_data.vendor_code = logs.vendor_code
          AND processed_data.line_user_id = logs.line_user_id
          AND processed_data.verfication_status = logs.msg_content
    WHERE logs.vendor_code IS NULL
    """

try:
  dataframe = query_BQ_table(query)
  # print("Created dataframe successfully")
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_vendor_verification_status_communication*: Failed to get data: ' + str(e)})
  # print("Cannot create dataframe")
  # print(e)

try:
  reponse_code_list, msg_content = send_line_vendor_verification_status_communication(url, headers, 
                                                                                      json_object_success,
                                                                                      json_object_not_success,
                                                                                      dataframe)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_vendor_verification_status_communication*: Failed send API request: ' + str(e)})

try:
  df = dataframe.filter(items=['vendor_code', 'line_user_id'])
  df["return_response"] = reponse_code_list
  df["msg_sent_date_time"] = now
  df["template_id_if_any"] = "line_vendor_verification_status_communication"
  df["msg_url"] = url
  df["msg_content"] = msg_content
  df_records = df.to_dict('records')
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_vendor_verification_status_communication*: Failed to record logs: ' + str(e)})
  # print(e)
