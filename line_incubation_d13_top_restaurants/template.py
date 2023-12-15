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
          "url": "https://drive.google.com/uc?export=view&id=1HMamUOxzXxRuTDdoo0pj7f8sr190hLtK",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "130:139",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "คลิก",
            "uri": "http://bit.ly/3lV9jFk"
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
                "uri": "http://bit.ly/3M0CcL1"
              },
              "color": "#FF2B85FF",
              "height": "sm",
              "style": "primary"
            }
          ]
        }
      }
    }
  ]
}

"""