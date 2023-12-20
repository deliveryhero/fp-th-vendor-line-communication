json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "จัดการออเดอร์บนแท็บเล็ตโกดรอยได้ง่ายๆ",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://drive.google.com/uc?export=view&id=16kCMxCEPWOJ2nX4watdFkyl3g0CZjNOX",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "20:21",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ดูวิดีโอการจัดการออเดอร์ทุกกรณี คลิก!",
              "size": "xs",
              "align": "center",
              "style": "italic",
              "action": {
                "type": "uri",
                "label": "action",
                "uri": "https://youtube.com/playlist?list=PLWLrh3ZaezZwslWrTmJ2uXpIVX3wh_F7o&si=qkd4OBzlFQOIzn_m"
              }
            }
          ],
          "backgroundColor": "#F7C6CC",
          "cornerRadius": "lg",
          "paddingAll": "sm",
          "action": {
            "type": "uri",
            "label": "action",
            "uri": "https://youtube.com/playlist?list=PLWLrh3ZaezZwslWrTmJ2uXpIVX3wh_F7o&si=xKOtOf0PnvEAb9nR"
          },
          "alignItems": "center"
        }
      }
    }
  ]
}

"""