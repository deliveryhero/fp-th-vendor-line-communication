import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="a")
                    
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from bigquery_data import query_BQ_table, record_line_communication_logs
from send_line_message import send_request_line_api, send_request_line_api_v2
from get_secrete_token import get_secret_data
import datetime, pytz



# Basic configuration tables
query_table = "fulfillment-dwh-production.pandata_report.country_TH_vendor_experience_Line_D7_no_valid_order"
line_data  = "foodpanda-th-bigquery.pandata_th.vendor_experience_line_liff_user_data_backup"
logs_table_id = "foodpanda-th-bigquery.pandata_th_external.line_communication_logs_live"

# Basic configuration parameters
Live = True
url = "https://api.line.me/v2/bot/message/push"
json_data = {
    "to": "lineuserid",
    "messages": [
        {
            "type": "flex",
            "altText": "อยากมีออเดอร์แรกต้องทำอย่างไร?",
            "contents":
{
  "type": "bubble",
  "size": "mega",
  "hero": {
    "type": "video",
    "url": "https://drive.google.com/uc?export=view&id=1DzWnB76ftyYOdlu6UxDMp2FY0TJvVEpa",
    "previewUrl": "https://drive.google.com/uc?export=view&id=1Jhx_bm8PZLnVBsWhkjyM55bKQKsk-Jom",
    "altContent": {
      "type": "image",
      "size": "full",
      "aspectRatio": "1284:2273",
      "aspectMode": "fit",
      "backgroundColor": "#F7C6CC",
      "url": "https://example.com/image.png"
   },
    "aspectRatio": "1284:2273"
  },
 "body": {
    "type": "box",
    "layout": "vertical",
    "backgroundColor": "#F7C6CC",
    "borderColor": "#F7C6CC",
    "contents": [
      {
        "type": "text",
        "text": "☝คลิกด้านบน เพื่อดูวิดีโอ☝",
        "size": "sm",
        "align": "center",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "xl",
        "color": "#F7C6CC"
      },
      {
        "type": "text",
        "text": "ได้ออเดอร์แรกไม่ใช่เรื่องยาก!",
        "weight": "bold",
        "size": "lg",
        "color": "#FF2B85",
        "align": "center",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "👉เพิ่มรูปภาพให้ครบทุกเมนู คลิก",
        "wrap": True,
        "action": {
          "type": "uri",
          "label": "คลิก",
          "uri": "http://bit.ly/3wVcPBA"
        },
        "contents": [
          {
            "type": "span",
            "text": "👉เพิ่มรูปภาพให้ครบทุกเมนู "
          },
          {
            "type": "span",
            "text": "คลิก",
            "color": "#FF2B85",
            "weight": "bold"
          }
        ]
      },
      {
        "type": "text",
        "text": "👉เปิดบิลได้ไวขึ้นด้วยเครื่องมือการตลาด คลิก",
        "wrap": True,
        "action": {
          "type": "uri",
          "label": "คลิก",
          "uri": "http://bit.ly/3DIneEp"
        },
        "contents": [
          {
            "type": "span",
            "text": "👉เปิดบิลได้ไวขึ้นด้วยเครื่องมือการตลาด "
          },
          {
            "type": "span",
            "text": "คลิก",
            "color": "#FF2B85",
            "weight": "bold"
          }
        ]
      },
      {
        "type": "text",
        "text": "👉ขยายเวลาทำการให้มากขึ้น คลิก",
        "wrap": True,
        "action": {
          "type": "uri",
          "label": "คลิก",
          "uri": "http://bit.ly/3jyEk0J"
        },
        "contents": [
          {
            "type": "span",
            "text": "👉ขยายเวลาทำการให้มากขึ้น "
          },
          {
            "type": "span",
            "text": "คลิก",
            "color": "#FF2B85",
            "weight": "bold"
          }
        ]
      }
    ]
  }
}
    }
  ]
}

json_string = str(json_data)

token = get_secret_data()
headers = {'Authorization': "Bearer {" + token + "}", 'Content-Type': 'application/json'}
tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if Live == False:
    query = f"""
    SELECT 
        vendor_data.vendor_code AS vendor_code,
        'U2b9495e231b925da2ed4163beeef6dad' AS line_user_id,
    FROM {query_table}  AS vendor_data
    INNER JOIN {line_data} AS line_data
            ON lower(line_data.VendorCode) = lower(vendor_data.vendor_code)
    LIMIT 1
    """

if Live == True:
    query = f"""
    SELECT DISTINCT
        vendor_data.vendor_code AS vendor_code,
        line_data.LineUserID AS line_user_id,
    FROM {query_table}  AS vendor_data
    INNER JOIN {line_data} AS line_data
            ON lower(line_data.VendorCode) = lower(vendor_data.vendor_code)
    """

try: 
  dataframe = query_BQ_table(query)
  user_id_list = dataframe["line_user_id"].tolist()
except BaseException as e:
    logging.info('Failed to get data: ' + str(e))

try:
  reponse_code_list, json_list = send_request_line_api_v2(url, headers, json_data, user_id_list)
except BaseException as e:
    logging.info('Failed send API request: ' + str(e))

dataframe["return_response"] = reponse_code_list
dataframe["msg_sent_date_time"] = now
dataframe["template_id_if_any"] = "Line_D7_no_valid_order"
dataframe["msg_url"] = url
dataframe["msg_content"] = json_list
df_records = dataframe.to_dict('records')

try:
  status = record_line_communication_logs(logs_table_id, df_records)
except BaseException as e:
    logging.info('Failed to record logs: ' + str(e))

logging.info(status)