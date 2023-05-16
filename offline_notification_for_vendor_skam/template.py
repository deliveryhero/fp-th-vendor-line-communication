json_object = """
{
    "to": "{line_user_id}",
    "messages": [
        {
            "type": "flex",
            "altText": "ร้านของคุณปิด ทำให้มีเวลาออฟไลน์",
            "contents":
    "type": "box",
    "layout": "vertical",
    "height": "380px",
    "contents": [{
  "type": "bubble",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://drive.google.com/uc?export=view&id=1t-_pm0agkInZxubSfHTv_pCyRsGxKNkc",
    "size": "full",
    "aspectRatio": "4:4",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://bit.ly/3RM70Ae"
    }
  },
  "body": {

      {
        "type": "text",
        "text": "ทีม foodpanda ได้ทำการเฝ้าสังเกตใน 1 สัปดาห์ที่ผ่านมา และพบว่าร้าน {vendor_name} ได้มีการปิดในเวลาทำการดังต่อไปนี้",
        "align": "start",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "ทีม foodpanda ได้ทำการเฝ้าสังเกตใน 1 สัปดาห์ที่ผ่านมา และพบว่า"
          },
          {
            "type": "span",
            "text": "ร้าน {vendor_name}",
            "color": "#FF2B85",
            "weight": "bold"
          },
          {
            "type": "span",
            "text": "ได้มีการปิดในเวลาทำการดังต่อไปนี้"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#FFFFFFFF"
      },
      {
        "type": "text",
        "text": "ข้อมูลวันที่ {start_date} ถึง {end_date}",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "ข้อมูลวันที่"
          },
          {
            "type": "span",
            "text": "{start_date} ถึง {end_date}",
            "color": "#FF2B85FF",
            "weight": "bold"
          }
        ]
      },
      {
        "type": "text",
        "text": "จำนวนชั่วโมงที่ปิดร้าน : {total_offline_hour} ชั่วโมง",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "จำนวนชั่วโมงที่ปิดร้าน :",
            "weight": "bold"
          },
          {
            "type": "span",
            "text": " {total_offline_hour} ชั่วโมง",
            "color": "#FF2B85FF",
            "weight": "bold"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg"
      },
      {
        "type": "text",
        "text": "หากสาขาของท่านมีปัญหาเกี่ยวกับแท็บเล็ต หรือสัญญาณอินเตอร์เน็ตสามารถติดต่อได้ที่ Hotline 02-4606021",
        "wrap": true,
        "contents": []
      }
    ]
  }
}
    }
  ]
}

"""