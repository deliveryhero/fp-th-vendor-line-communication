json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "อย่าลืม! เปลี่ยนสถานะร้าน หากร้านของคุณปิด!",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "hero": {
          "type": "image",
          "url": "https://bucket.ex10.tech/images/8bb98a34-2258-11ef-a8d5-0242ac120003/originalContentUrl.jpg",
          "size": "full",
          "aspectRatio": "4:4",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": "https://bit.ly/45NutWZ"
          }
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "เพิ่มวันหยุดเลย คลิก",
                "uri": "https://tinyurl.com/AutoCommsOPTimess"
              },
              "style": "primary",
              "color": "#FF2B85"
            }
          ]
        }
      }
    }
  ],
  "customAggregationUnits": [
    "RestaurantClose"
  ]
}

"""