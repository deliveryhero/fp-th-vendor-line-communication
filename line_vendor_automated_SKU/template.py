json_object = """

{
    "to": "{line_user_id}",
    "messages": [
        {
            "type": "flex",
            "altText": "อยากเพิ่มโอกาสให้ลูกค้าสั่งซื้อมากขึ้นต้องลอง!",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://drive.google.com/uc?export=view&id=1Rnvk5FJ2QU4SynXn4ZwPcLBUzW2WJPgR",
    "size": "full",
    "aspectRatio": "130:161",
    "aspectMode": "cover"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "secondary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "ดูวิธีเพิ่มเมนู คลิก",
          "text": "410"
        },
        "color": "#FFD271"
      },
      {
        "type": "button",
        "style": "secondary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "เพิ่มเมนูตอนนี้ คลิก",
          "uri": "https://bit.ly/3N9HmnE"
        },
        "color": "#FFD271"
      }
    ],
    "flex": 0,
    "borderColor": "#FFFFFF"
  },
  "styles": {
    "footer": {
      "backgroundColor": "#FF2B85"
    }
  }
}
    }
  ],
    "customAggregationUnits": [
        "SKU"]
}

"""