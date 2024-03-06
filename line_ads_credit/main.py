import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_ads_credit
from get_secrete_token import get_secret_data
import datetime, pytz
import requests
from template import json_object

# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_insider_ads_credit_vendors"
vendor_table = "fulfillment-dwh-production.pandata_report.country_TH_general_pd_vendors"
line_liff_table = "foodpanda-th-bigquery.pandata_th_external.vendor_experience_line_liff_user_data"
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

      SELECT
        target_vendors.vendor_code,
        IFNULL(th_vendors.vendor_name_th, th_vendors.vendor_name_en) AS vendor_name,
        CAST(FORMAT("%'d", CAST(target_vendors.recommended_budget AS INT)) AS STRING) AS recommended_budget,
        "Uca11d4d4585c435204950dba18dafcd8" AS line_user_id
      FROM `{query_table}` AS target_vendors
      INNER JOIN `{vendor_table}` AS th_vendors
              ON th_vendors.vendor_code = target_vendors.vendor_code
      INNER JOIN line_verification
              ON line_verification.vendor_code = target_vendors.vendor_code
      LIMIT 1
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

      SELECT
        target_vendors.vendor_code,
        IFNULL(th_vendors.vendor_name_th, th_vendors.vendor_name_en) AS vendor_name,
        CAST(FORMAT("%'d", CAST(target_vendors.recommended_budget AS INT)) AS STRING) AS recommended_budget,
        line_verification.line_user_id
      FROM `{query_table}` AS target_vendors
      INNER JOIN `{vendor_table}` AS th_vendors
              ON th_vendors.vendor_code = target_vendors.vendor_code
      INNER JOIN line_verification
              ON line_verification.vendor_code = target_vendors.vendor_code
    """

try:
  dataframe = query_BQ_table(query)
  # print("Created dataframe successfully")
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_ads_credit*: Failed to get data: ' + str(e)})
  # print("Cannot create dataframe")

try:
  reponse_code_list, json_list = send_request_line_api_ads_credit(url = url,
                                                          headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_ads_credit*: Failed send API request: ' + str(e)})
  # print(e)

try:
  df = dataframe.filter(items=['vendor_code', 'line_user_id'])
  df["return_response"] = reponse_code_list
  df["msg_sent_date_time"] = now
  df["template_id_if_any"] = "line_ads_credit"
  df["msg_url"] = url
  df["msg_content"] = 'content vendor_code: ' + dataframe['vendor_code'] \
                      +','+'content vendor_name: ' + dataframe['vendor_name'] \
                      +','+'content recommended_budget: ' + dataframe['recommended_budget']
  df_records = df.to_dict('records')
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_ads_credit*: Failed to record logs: ' + str(e)})
  # print(e)
