json_object = """
{
    "to": "{line_user_id}",
    "messages": [
        {
            "type": "flex",
            "altText": "ร้านของคุณปิด ทำให้มีเวลาออฟไลน์",
            "contents":
{
  "type": "bubble",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://drive.google.com/uc?export=view&id=1zIUw4Dylda6vO-Qn83-JdL3kN2wi5tOD",
    "size": "full",
    "aspectRatio": "7.5:3",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://foodpanda.portal.restaurant/opening-times-pandora?int_ref=side-nav"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
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
            "text": "ร้าน {vendor_name} ",
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
        "text": "ข้อมูลวันที่ {start_date_in_thai} ถึง {end_date_in_thai}",
        "weight": "bold",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "ข้อมูลวันที่"
          },
          {
            "type": "span",
            "text": " {start_date_in_thai} ถึง {end_date_in_thai}",
            "color": "#FF2B85FF",
            "weight": "bold"
          }
        ]
      },
      {
        "type": "text",
        "text": "จำนวนชั่วโมงที่ปิดร้าน : {total_offline_hours} ชั่วโมง",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "จำนวนชั่วโมงที่ปิดร้าน :",
            "weight": "bold"
          },
          {
            "type": "span",
            "text": " {total_offline_hours} ชั่วโมง",
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
        "text": "หากสาขาของท่านมีปัญหาเกี่ยวกับแท็บเล็ต หรือสัญญาณอินเทอร์เน็ต สามารถติดต่อฝ่ายให้บริการร้านได้ทุกวัน ตั้งแต่เวลา 09:00 น. - 21:00 น.ได้ที่เบอร์: 02-460-6020",
        "wrap": true,
        "contents": []
      }
    ]
  }
}
    }
  ],
    "customAggregationUnits": [
        "OfflineNotificationForVendorSKAM"
    ]
}


"""