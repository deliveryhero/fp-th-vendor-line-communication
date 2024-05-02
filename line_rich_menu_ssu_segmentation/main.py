import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api_rich_menu_ssu_segmentation
from get_secrete_token import get_secret_data
import datetime, pytz
import requests

# Basic configuration tables
query_table_vendor = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_ssu_vendor_segmentation"
line_data  = "foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup"
pii_data = "foodpanda-th-bigquery.pandata_th.sf_account_internal_non_pii"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

# Basic configuration parameters
slack_webhook = os.getenv('slack_webhook')
Live = True
vendor_menu_new_url = "https://api.line.me/v2/bot/user/user_id_variable/richmenu/richmenu-0c474898e19216646ffdbb422e11e0d0"
vendor_menu_failed_url = "https://api.line.me/v2/bot/user/user_id_variable/richmenu/richmenu-61a444a9532d9939bd6673ea83952993"
vendor_lost_url = "https://api.line.me/v2/bot/user/user_id_variable/richmenu/richmenu-ba158eede83289e2274eb1d6043d91a5"
vendor_onboarding_url = "https://api.line.me/v2/bot/user/user_id_variable/richmenu/richmenu-e5cab4c05afdac4981cd7315bb80b598"
vendor_active_url = "https://api.line.me/v2/bot/user/user_id_variable/richmenu/richmenu-508759517fcd4c522f5f1b8842bfb91c"
vendor_menu_new_template = "richmenu-0c474898e19216646ffdbb422e11e0d0"
vendor_menu_failed_template = "richmenu-61a444a9532d9939bd6673ea83952993"
vendor_lost_template = "richmenu-ba158eede83289e2274eb1d6043d91a5"
vendor_onboarding_template = "richmenu-e5cab4c05afdac4981cd7315bb80b598"
vendor_active_template = "richmenu-508759517fcd4c522f5f1b8842bfb91c"

rich_menu_urls = [vendor_menu_new_url, vendor_menu_failed_url, vendor_lost_url, vendor_onboarding_url, vendor_active_url]
templates_list = [vendor_menu_new_template, vendor_menu_failed_template, vendor_lost_template, vendor_onboarding_template, vendor_active_template]


token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}", 'Content-Type': 'application/json'}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
    WITH line_logs AS (
    SELECT 
      *
    FROM `foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live` AS logs
    WHERE CONTAINS_SUBSTR(logs.template_id_if_any, 'richmenu')
    QUALIFY ROW_NUMBER() OVER(PARTITION BY vendor_code, line_user_id ORDER BY msg_sent_date_time DESC) = 1
    )

    SELECT
      segemnt.vendor_code,
      segemnt.menu_case_number,
      segemnt.ssu_vendor_status,
      "U2b9495e231b925da2ed4163beeef6dad" AS line_user_id
    FROM `fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_ssu_vendor_segmentation` AS segemnt
    INNER JOIN `foodpanda-th-bigquery.pandata_th_external.vendor_experience_line_liff_user_data` AS line_data
            ON LOWER(segemnt.vendor_code) = LOWER(line_data.VendorCode)
    INNER JOIN `foodpanda-th-bigquery.pandata_th.sf_account_internal_non_pii` AS pii_data
            ON pii_data.vendor_code = segemnt.vendor_code
            AND pii_data.account_phone = IF(LENGTH(line_data.VendorMobile) = 9,
                                            CONCAT("+66", line_data.VendorMobile),
                                            REGEXP_REPLACE(TRIM(LOWER(REPLACE(line_data.VendorMobile, "-", ""))), r"^0+", "+66"))
    LEFT JOIN line_logs AS logs
            ON logs.vendor_code = segemnt.vendor_code
          AND logs.line_user_id = line_data.LineUserID
          AND CONTAINS_SUBSTR(logs.template_id_if_any, 'richmenu')
    LEFT JOIN line_logs AS logs2
           ON logs2.line_user_id = line_data.LineUserID
          AND CONTAINS_SUBSTR(logs2.template_id_if_any, 'richmenu')
    WHERE line_data.LineUserID IS NOT NULL
      AND (logs.template_id_if_any IS NULL OR logs2.template_id_if_any != "richmenu-508759517fcd4c522f5f1b8842bfb91c")
      AND (logs.msg_content IS NULL OR  segemnt.ssu_vendor_status != logs.msg_content)
      AND segemnt.ssu_vendor_status != "Undefined"
    QUALIFY ROW_NUMBER() OVER (PARTITION BY line_data.LineUserID ORDER BY segemnt.ssu_vendor_status) = 1
        LIMIT 1
    """

if Live == True:
    query = f"""
    WITH line_logs AS (
    SELECT 
      *
    FROM `foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live` AS logs
    WHERE CONTAINS_SUBSTR(logs.template_id_if_any, 'richmenu')
    QUALIFY ROW_NUMBER() OVER(PARTITION BY vendor_code, line_user_id ORDER BY msg_sent_date_time DESC) = 1
    )

    SELECT
      segemnt.vendor_code,
      segemnt.menu_case_number,
      segemnt.ssu_vendor_status,
      line_data.LineUserID AS line_user_id
    FROM `fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_ssu_vendor_segmentation` AS segemnt
    INNER JOIN `foodpanda-th-bigquery.pandata_th_external.vendor_experience_line_liff_user_data` AS line_data
            ON LOWER(segemnt.vendor_code) = LOWER(line_data.VendorCode)
    INNER JOIN `foodpanda-th-bigquery.pandata_th.sf_account_internal_non_pii` AS pii_data
            ON pii_data.vendor_code = segemnt.vendor_code
            AND pii_data.account_phone = IF(LENGTH(line_data.VendorMobile) = 9,
                                            CONCAT("+66", line_data.VendorMobile),
                                            REGEXP_REPLACE(TRIM(LOWER(REPLACE(line_data.VendorMobile, "-", ""))), r"^0+", "+66"))
    LEFT JOIN line_logs AS logs
            ON logs.vendor_code = segemnt.vendor_code
          AND logs.line_user_id = line_data.LineUserID
          AND CONTAINS_SUBSTR(logs.template_id_if_any, 'richmenu')
    LEFT JOIN line_logs AS logs2
           ON logs2.line_user_id = line_data.LineUserID
          AND CONTAINS_SUBSTR(logs2.template_id_if_any, 'richmenu')
    WHERE line_data.LineUserID IS NOT NULL
      AND (logs.template_id_if_any IS NULL OR logs2.template_id_if_any != "richmenu-508759517fcd4c522f5f1b8842bfb91c")
      AND (logs.msg_content IS NULL OR  segemnt.ssu_vendor_status != logs.msg_content)
      AND segemnt.ssu_vendor_status != "Undefined"
    QUALIFY ROW_NUMBER() OVER (PARTITION BY line_data.LineUserID ORDER BY segemnt.ssu_vendor_status) = 1
    """

try: 
  dataframe = query_BQ_table(query)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_rich_menu_ssu_segmentation*: Failed to get data: ' + str(e)})

try:
  reponse_code_list, url_list, template_list = send_request_line_api_rich_menu_ssu_segmentation(rich_menu_urls, templates_list, headers, dataframe)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_rich_menu_ssu_segmentation*: Failed send API request: ' + str(e)})

try:
  dataframe1 = dataframe.filter(items=['vendor_code', 'line_user_id'])
  dataframe1["return_response"] = reponse_code_list
  dataframe1["msg_sent_date_time"] = now
  dataframe1["template_id_if_any"] = template_list
  dataframe1["msg_url"] = url_list
  dataframe1["msg_content"] = dataframe['ssu_vendor_status']
  df_records = dataframe1.to_dict('records')
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_rich_menu_ssu_segmentation*: Failed to record logs: ' + str(e)})
