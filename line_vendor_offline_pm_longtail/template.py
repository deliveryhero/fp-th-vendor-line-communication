json_object = """
{
    "to": "{line_user_id}",
    "messages": [
        {
            "type": "flex",
            "altText": "เรามาเพื่อเตือน! อย่าให้ลูกค้าขาดความเชื่อมั่น",
            "contents":
{
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
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ภายในวันที่",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "ภายในวันที่"
          },
          {
            "type": "span",
            "text": " {start_date_in_thai} ถึง {end_date_in_thai} ",
            "color": "#FF2B85FF",
            "weight": "bold"
          },
          {
            "type": "span",
            "text": "ทีม foodpanda สังเกตเห็นว่า "
          },
          {
            "type": "span",
            "text": "ร้าน {vendor_name} ",
            "color": "#FF2B85FF",
            "weight": "bold"
          },
          {
            "type": "span",
            "text": "ได้ปิดร้านในเวลาทำการจำนวน "
          },
          {
            "type": "span",
            "text": "{total_offline_hours} ชั่วโมง ",
            "color": "#FF2B85FF",
            "weight": "bold"
          },
          {
            "type": "span",
            "text": "ทำให้คุณพลาดโอกาสที่จะได้รับออเดอร์จำนวน "
          },
          {
            "type": "span",
            "text": "{potential_order_loss} ออเดอร์",
            "color": "#FF2B85FF",
            "weight": "bold"
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
        "text": "หากร้านของคุณมีปัญหาเกี่ยวกับแท็บเล็ต หรือสัญญาณอินเตอร์เน็ตสามารถส่งคำร้อง ที่นี่!",
        "wrap": true,
        "action": {
          "type": "uri",
          "label": "ที่นี่!",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSeJeHgum4Pn34DKVHv5uwF67GHaqEdhgzCb0BlxV2Z1CunXFw/viewform"
        },
        "contents": [
          {
            "type": "span",
            "text": "หากร้านของคุณมีปัญหาเกี่ยวกับแท็บเล็ต หรือสัญญาณอินเตอร์เน็ตสามารถส่งคำร้อง "
          },
          {
            "type": "span",
            "text": "ที่นี่!",
            "color": "#FF2B85FF",
            "weight": "bold",
            "decoration": "underline"
          }
        ]
      }
    ]
  }
}
    }
  ],
    "customAggregationUnits": [
        "OfflineNotificationForVendorPMLongtail"
    ]
}

"""