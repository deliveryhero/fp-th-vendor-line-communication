import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_generic_reminder
from get_secrete_token import get_secret_data
import datetime, pytz
import requests
from template import json_object

# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_auto_first_failed_orders_sms"
line_liff_table = "foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"
targeted_failed_reasons = "VENDOR_UNREACHABLE"
pipeline_name = "line_first_failed_unreachable"

# Basic configuration parameters
slack_webhook = os.getenv('slack_webhook')
Live = True
url = "https://api.line.me/v2/bot/message/push"

token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}", 'Content-Type': 'application/json'}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

# if Live == False:
#     query = f"""
#       WITH line_verification AS (
#         SELECT
#           TRIM(LOWER(VendorCode)) AS vendor_code,
#           LineUserID AS line_user_id
#         FROM `{line_liff_table}`
#         WHERE date IS NOT NULL
#           AND LineUserID IS NOT NULL
#         QUALIFY ROW_NUMBER() OVER (
#           PARTITION BY
#             vendor_code,
#             line_user_id
#           ORDER BY
#             date DESC
#         ) = 1
#       )

#       SELECT DISTINCT
#         vendors.vendor_code,
#         "Uca11d4d4585c435204950dba18dafcd8" AS line_user_id
#       FROM `{query_table}` AS vendors
#       LEFT JOIN line_verification
#              ON line_verification.vendor_code = vendors.vendor_code
#       WHERE DATE(vendors.report_datetime_local) = CURRENT_DATE("Asia/Bangkok")
#         AND vendors.decline_reason = "{targeted_failed_reasons}"
#         AND line_verification.line_user_id IS NOT NULL
#       LIMIT 1
#     """

if Live == False:
    query = f"""
      SELECT
        "test" AS vendor_code,
        "Uca11d4d4585c435204950dba18dafcd8" AS line_user_id
    """

if Live == True:
    query = f"""
      WITH line_verification AS (
        SELECT
          TRIM(LOWER(VendorCode)) AS vendor_code,
          LineUserID AS line_user_id
        FROM `{line_liff_table}`
        WHERE date IS NOT NULL
          AND LineUserID IS NOT NULL
        QUALIFY ROW_NUMBER() OVER (
          PARTITION BY
            vendor_code,
            line_user_id
          ORDER BY
            date DESC
        ) = 1
      )

      SELECT DISTINCT
        vendors.vendor_code,
        line_verification.line_user_id
      FROM `{query_table}` AS vendors
      LEFT JOIN line_verification
             ON line_verification.vendor_code = vendors.vendor_code
      WHERE DATE(vendors.report_datetime_local) = CURRENT_DATE("Asia/Bangkok")
        AND vendors.decline_reason = "{targeted_failed_reasons}"
        AND line_verification.line_user_id IS NOT NULL
    """

try:
  dataframe = query_BQ_table(query)
  # print("Created dataframe successfully")
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*{pipeline_name}*: Failed to get data: ' + str(e)})
  # print("Cannot create dataframe")
  # print(e)

try:
  reponse_code_list, json_list = send_request_line_api_generic_reminder(url = url,
                                                          headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*{pipeline_name}*: Failed send API request: ' + str(e)})

try:
  df = dataframe.filter(items=['vendor_code', 'line_user_id'])
  df["return_response"] = reponse_code_list
  df["msg_sent_date_time"] = now
  df["template_id_if_any"] = pipeline_name
  df["msg_url"] = url
  df["msg_content"] = pipeline_name
  df_records = df.to_dict('records')
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*{pipeline_name}*: Failed to record logs: ' + str(e)})
  # print(e)
