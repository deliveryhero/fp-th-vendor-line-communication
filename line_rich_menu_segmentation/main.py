import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_rich_menu_segment_messages
from get_secrete_token import get_secret_data
import datetime, pytz
import requests

# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_Line_rich_menu_segmented_report"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

# Basic configuration parameters
slack_webhook = os.getenv('slack_webhook')
Live = False
url = "https://api.line.me/v2/bot/user/user_id_variable/richmenu/template_id_variable"
json = {}
token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}"}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
    DECLARE testid STRING DEFAULT 'U9d1f00f6f00199356eee821cb2736ac2'; 
    SELECT 
      segment.vendor_code,
      testid AS line_user_id,
      segment.segment_rank,
      segment.segment_name,
      CASE
        WHEN segment.segment_rank = 1 THEN "richmenu-ae465e30fde5a0c30f2dcd9c0c32d0c3"
        WHEN segment.segment_rank = 2 THEN "richmenu-93b61452c89ea40c5aa7a6c798388f4a"
        WHEN segment.segment_rank = 3 THEN "richmenu-58bd6e191e4228cfc1d045c921f378d7"
        WHEN segment.segment_rank = 4 THEN "richmenu-49db240f4d2212e4756f875fc53f3918"
        WHEN segment.segment_rank = 5 THEN "richmenu-956941cfc42cdea9efc0ac9b6f4bee25"
      END AS richmenu_template_id,
      CASE
        WHEN segment.segment_rank = 1 
          THEN CONCAT("https://api.line.me/v2/bot/user/",testid,"/richmenu/","richmenu-ae465e30fde5a0c30f2dcd9c0c32d0c3")
        WHEN segment.segment_rank = 2 
          THEN CONCAT("https://api.line.me/v2/bot/user/",testid,"/richmenu/","richmenu-93b61452c89ea40c5aa7a6c798388f4a")
        WHEN segment.segment_rank = 3 
          THEN CONCAT("https://api.line.me/v2/bot/user/",testid,"/richmenu/","richmenu-58bd6e191e4228cfc1d045c921f378d7")
        WHEN segment.segment_rank = 4 
          THEN CONCAT("https://api.line.me/v2/bot/user/",testid,"/richmenu/","richmenu-49db240f4d2212e4756f875fc53f3918")
        WHEN segment.segment_rank = 5 
          THEN CONCAT("https://api.line.me/v2/bot/user/",testid,"/richmenu/","richmenu-956941cfc42cdea9efc0ac9b6f4bee25")
      END AS line_rich_menu_url,
      CONCAT("Segment: ", segment.segment_rank, "-", segment.segment_name) AS msg_content
    FROM {query_table} AS segment
    INNER JOIN {logs_table_id} AS line_logs
            ON line_logs.vendor_code = segment.vendor_code
    WHERE line_logs.template_id_if_any = "richmenu-6da47a1cac4c62cc569bf5efdef303eb"
      AND EXTRACT(DATE FROM line_logs.msg_sent_date_time) = DATE_SUB(CURRENT_DATE(),INTERVAL 1 DAY)
      AND segment.segment_rank = 5
    LIMIT 1
    """

if Live == True:
    query = f"""
    SELECT 
      segment.vendor_code,
      line_logs.line_user_id,
      segment.segment_rank,
      segment.segment_name,
      CASE
        WHEN segment.segment_rank = 1 THEN "richmenu-ae465e30fde5a0c30f2dcd9c0c32d0c3"
        WHEN segment.segment_rank = 2 THEN "richmenu-93b61452c89ea40c5aa7a6c798388f4a"
        WHEN segment.segment_rank = 3 THEN "richmenu-58bd6e191e4228cfc1d045c921f378d7"
        WHEN segment.segment_rank = 4 THEN "richmenu-49db240f4d2212e4756f875fc53f3918"
        WHEN segment.segment_rank = 5 THEN "richmenu-956941cfc42cdea9efc0ac9b6f4bee25"
      END AS richmenu_template_id,
      CASE
        WHEN segment.segment_rank = 1 
          THEN CONCAT("https://api.line.me/v2/bot/user/",line_logs.line_user_id,"/richmenu/","richmenu-ae465e30fde5a0c30f2dcd9c0c32d0c3")
        WHEN segment.segment_rank = 2 
          THEN CONCAT("https://api.line.me/v2/bot/user/",line_logs.line_user_id,"/richmenu/","richmenu-93b61452c89ea40c5aa7a6c798388f4a")
        WHEN segment.segment_rank = 3 
          THEN CONCAT("https://api.line.me/v2/bot/user/",line_logs.line_user_id,"/richmenu/","richmenu-58bd6e191e4228cfc1d045c921f378d7")
        WHEN segment.segment_rank = 4 
          THEN CONCAT("https://api.line.me/v2/bot/user/",line_logs.line_user_id,"/richmenu/","richmenu-49db240f4d2212e4756f875fc53f3918")
        WHEN segment.segment_rank = 5 
          THEN CONCAT("https://api.line.me/v2/bot/user/",line_logs.line_user_id,"/richmenu/","richmenu-956941cfc42cdea9efc0ac9b6f4bee25")
      END AS line_rich_menu_url,
      CONCAT("Segment: ", segment.segment_rank, "-", segment.segment_name) AS msg_content
    FROM {query_table} AS segment
    INNER JOIN {logs_table_id} AS line_logs
            ON line_logs.vendor_code = segment.vendor_code
    WHERE line_logs.template_id_if_any = "richmenu-6da47a1cac4c62cc569bf5efdef303eb"
      AND EXTRACT(DATE FROM line_logs.msg_sent_date_time) = DATE_SUB(CURRENT_DATE(),INTERVAL 1 DAY)
    """

try: 
  dataframe = query_BQ_table(query)
  line_segment_urls = dataframe["line_rich_menu_url"].tolist()
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_richmenu_segmentation_message*: Failed to get data: ' + str(e)})

try:
  reponse_code_list = send_request_line_rich_menu_segment_messages(url = line_segment_urls, headers = headers)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_richmenu_segmentation_message*: Failed send API request: ' + str(e)})

dataframe1 = dataframe.filter(items=['vendor_code', 'line_user_id', 'msg_content'])
dataframe1["return_response"] = reponse_code_list
dataframe1["msg_sent_date_time"] = now
dataframe1["template_id_if_any"] = dataframe['richmenu_template_id']
dataframe1["msg_url"] = dataframe["line_rich_menu_url"]
df_records = dataframe1.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    requests.post(slack_webhook,
    json = {'text' : '*line_richmenu_segmentation_message*: Failed to record logs: ' + str(e)})
