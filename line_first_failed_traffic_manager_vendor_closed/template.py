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
          "url": "https://bucket.ex10.tech/images/f3af3e86-223f-11ef-a8d5-0242ac120003/originalContentUrl.jpg",
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