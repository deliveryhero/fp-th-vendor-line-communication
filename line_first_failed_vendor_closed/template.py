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
          "url": "https://drive.google.com/uc?export=view&id=1_QIYRnle9G2LTusWtTrdeWeNqsmC1s3x",
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
                "uri": "https://bit.ly/3Qutbuz"
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
    "SMS"
  ]
}

"""