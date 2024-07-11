json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "โดดเด่นกว่าร้านอื่น ด้วยโปรแกรม สุดยอดร้านอาหาร",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://bucket.ex10.tech/images/4385b305-3a9a-11ef-891c-0242ac120003/originalContentUrl.jpg",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "130:139",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "คลิก",
            "uri": "https://tinyurl.com/AutoCommsRP"
          }
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "เรียนรู้เพิ่มเติม",
                "uri": "https://tinyurl.com/AutoCommsUnigd"
              },
              "color": "#FF2B85FF",
              "height": "sm",
              "style": "primary"
            }
          ]
        }
      }
    }
  ],
  "customAggregationUnits": [
    "Incud20"
  ]
}

"""