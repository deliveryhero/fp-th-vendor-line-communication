json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "เปิดทำการอยู่ แต่ไรเดอร์หาร้านไม่เจอ?!",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "hero": {
          "type": "image",
          "url": "https://drive.google.com/uc?export=view&id=13SxyHvOYqPYC2Tdk6tWWuLGkAWS8_KT7",
          "size": "full",
          "aspectRatio": "4:4",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": "https://bit.ly/3ScwlFG"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ดูวิธีการเปลี่ยนที่อยู่ร้าน คลิก",
                "uri": "https://bit.ly/3S7S41r"
              },
              "color": "#FF2B85",
              "style": "primary"
            }
          ]
        }
      }
    }
  ],
  "customAggregationUnits": [
    "RiderCannotFind"
  ]
}

"""