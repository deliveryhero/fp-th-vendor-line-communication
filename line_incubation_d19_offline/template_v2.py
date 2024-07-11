json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "ตรวจสอบให้แน่ใจ! คุณเปิดร้านตรงกับเวลาทำการในระบบหรือไม่??",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://bucket.ex10.tech/images/8df734b9-3dd3-11ef-891c-0242ac120003/originalContentUrl.jpg",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "100:100",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ดูวิธีการจัดการบนโกดรอย/โกแอป คลิก",
              "action": {
                "type": "uri",
                "label": "ดูวิธีการจัดการบนโกดรอย/โกแอป คลิก",
                "uri": "https://tinyurl.com/AutoCommsytplgd"
              },
              "size": "sm",
              "style": "italic"
            }
          ],
          "backgroundColor": "#FFFFFF",
          "cornerRadius": "lg",
          "alignItems": "center",
          "paddingAll": "sm"
        },
        "styles": {
          "body": {
            "backgroundColor": "#F7C6CC"
          }
        }
      }
    }
  ],
  "customAggregationUnits": [
    "Incud15"
  ]
}

"""