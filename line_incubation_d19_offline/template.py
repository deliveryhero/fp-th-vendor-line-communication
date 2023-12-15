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
          "url": "https://drive.google.com/uc?export=view&id=1D9oBE6J3u5ajZe5I0KzrnQw0gCL-E23U",
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
                "uri": "https://youtube.com/playlist?list=PLWLrh3ZaezZwslWrTmJ2uXpIVX3wh_F7o&si=eVpazmIcZC2TNch4"
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
  ]
}

"""