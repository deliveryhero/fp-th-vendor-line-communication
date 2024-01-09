json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "สำคัญ! เช็กลิส 4 ข้อ เตรียมตัวให้พร้อมก่อนเปิดร้านบน foodpanda",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://drive.google.com/uc?export=view&id=1jJChl_Ugg4XvOp60FpFw7Xa5O6nk1hRj",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "20:21",
          "aspectMode": "cover",
          "action": {
            "type": "message",
            "label": "action",
            "text": "226"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "contents": [],
              "action": {
                "type": "uri",
                "label": "action",
                "uri": "https://youtube.com/playlist?list=PLWLrh3ZaezZwvTBYF3oydRjYFQqALze4J&si=vDS7SmjpMUD1vVTT"
              },
              "text": "ดูวิดีโอสำหรับมือใหม่เพื่อพร้อมเปิดร้านขายที่นี่ คลิก",
              "size": "sm",
              "align": "center",
              "style": "italic"
            }
          ],
          "cornerRadius": "lg",
          "backgroundColor": "#FFFFFF",
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