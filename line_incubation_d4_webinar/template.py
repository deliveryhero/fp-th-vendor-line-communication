json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "แบไต๋หมดเปลือก! เผยเคล็ดลับขายดี ร้านใหม่ห้ามพลาด!",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://drive.google.com/uc?export=view&id=1u4rLM9UISIDSOXnO82i1TiyEDWLT_CJK",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "20:20",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "คลิก",
            "uri": "http://bit.ly/3JOaSNy"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "align": "center",
              "wrap": true,
              "action": {
                "type": "uri",
                "label": "คลิก",
                "uri": "https://youtube.com/playlist?list=PLWLrh3ZaezZx6XFBylYkG_p1vZBCT_2Qs&si=x0QCv6bZKtFHaQ-K"
              },
              "contents": [],
              "text": "อยากเป็นมือโปร? ดูเครื่องมือโปรโมทร้านสุดปัง คลิก!",
              "size": "sm",
              "style": "italic"
            }
          ],
          "backgroundColor": "#FFFFFF",
          "cornerRadius": "lg",
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