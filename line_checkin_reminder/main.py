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
query_table = "foodpanda-th-bigquery.pandata_th.country_TH_vendor_experience_line_checkin_reminder"
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
      WITH vendor_agg_line_id AS (
        SELECT DISTINCT
          vendor_code,
          "Uca11d4d4585c435204950dba18dafcd8" AS line_user_id,
          CASE
            # scenario #1 - where the vendors open between 23:31 to 23:59 / separate task scheduler runs once at 23:59
            WHEN FORMAT_TIME("%H:%M", CURRENT_TIME("Asia/Bangkok")) = "23:59"
             AND opening_time BETWEEN "23:31:00" AND "23:59:00"
            THEN TRUE

            # scenario #2 - where the vendors open at midnight
            WHEN FORMAT_TIME("%H:%M", CURRENT_TIME("Asia/Bangkok")) = "00:01"
             AND opening_time = "00:00:00"
            THEN TRUE

            # scenario #3 - where the vendors open after midnight
            WHEN FORMAT_TIME("%H:%M", CURRENT_TIME("Asia/Bangkok")) != "23:59"
             AND FORMAT_TIME("%H:%M", CURRENT_TIME("Asia/Bangkok")) != "00:01"
             AND opening_time >= TIME_SUB(TIME(CURRENT_DATETIME("Asia/Bangkok")), INTERVAL 30 MINUTE)
             AND opening_time <= TIME_SUB(TIME(CURRENT_DATETIME("Asia/Bangkok")), INTERVAL 1 MINUTE)
            THEN TRUE

            ELSE FALSE
          END AS is_selected
        FROM {query_table}
        WHERE line_user_id IS NOT NULL
          AND DATE(recorded_at_local) = CURRENT_DATE("Asia/Bangkok")
      )

      SELECT
        *
      FROM vendor_agg_line_id
      WHERE is_selected
      LIMIT 1
    """

if Live == True:
    query = f"""
      WITH vendor_agg_line_id AS (
        SELECT DISTINCT
          vendor_code,
          line_user_id,
          CASE
            # scenario #1 - where the vendors open between 23:31 to 23:59 / separate task scheduler runs once at 23:59
            WHEN FORMAT_TIME("%H:%M", CURRENT_TIME("Asia/Bangkok")) = "23:59"
             AND opening_time BETWEEN "23:31:00" AND "23:59:00"
            THEN TRUE

            # scenario #2 - where the vendors open at midnight
            WHEN FORMAT_TIME("%H:%M", CURRENT_TIME("Asia/Bangkok")) = "00:01"
             AND opening_time = "00:00:00"
            THEN TRUE

            # scenario #3 - where the vendors open after midnight
            WHEN FORMAT_TIME("%H:%M", CURRENT_TIME("Asia/Bangkok")) != "23:59"
             AND FORMAT_TIME("%H:%M", CURRENT_TIME("Asia/Bangkok")) != "00:01"
             AND opening_time >= TIME_SUB(TIME(CURRENT_DATETIME("Asia/Bangkok")), INTERVAL 30 MINUTE)
             AND opening_time <= TIME_SUB(TIME(CURRENT_DATETIME("Asia/Bangkok")), INTERVAL 1 MINUTE)
            THEN TRUE

            ELSE FALSE
          END AS is_selected
        FROM {query_table}
        WHERE line_user_id IS NOT NULL
          AND DATE(recorded_at_local) = CURRENT_DATE("Asia/Bangkok")
      )

      SELECT
        *
      FROM vendor_agg_line_id
      WHERE is_selected
    """

try:
  dataframe = query_BQ_table(query)
  # print("Created dataframe successfully")
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_checkin_reminder*: Failed to get data: ' + str(e)})
  # print("Cannot create dataframe")
  # print(e)

try:
  reponse_code_list, json_list = send_request_line_api_generic_reminder(url = url,
                                                          headers = headers,
                                                          json_object = json_object,
                                                          dataframe = dataframe)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_checkin_reminder*: Failed send API request: ' + str(e)})

try:
  df = dataframe.filter(items=['vendor_code', 'line_user_id'])
  df["return_response"] = reponse_code_list
  df["msg_sent_date_time"] = now
  df["template_id_if_any"] = "line_checkin_reminder"
  df["msg_url"] = url
  df["msg_content"] = "line_checkin_reminder"
  df_records = df.to_dict('records')
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
  requests.post(slack_webhook,
  json = {'text' : '*line_checkin_reminder*: Failed to record logs: ' + str(e)})
  # print(e)
