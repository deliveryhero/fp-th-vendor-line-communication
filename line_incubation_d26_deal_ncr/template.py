json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "มาทำความรู้จักกับเครื่องมือโปรโมทร้านบน foodpanda กันเถอะ!",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://drive.google.com/uc?export=view&id=14Z3oO6AQpMEFilvWYmTFATQZjSScC2qm",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "100:100",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "คลิก",
            "uri": "http://bit.ly/3lOOonw"
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
                "label": "เรียนรู้การเงิน ",
                "uri": "https://youtube.com/playlist?list=PLWLrh3ZaezZwdvA4NCuY9ecdzpDK_Y9zx&si=TH8OAYbIK33RQdaE"
              },
              "color": "#FF2B85FF",
              "height": "sm",
              "style": "primary",
              "offsetStart": "none",
              "offsetEnd": "xs"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ลองเลย ",
                "uri": "http://bit.ly/3FSFfRt"
              },
              "color": "#FF2B85FF",
              "height": "sm",
              "style": "primary",
              "offsetEnd": "none",
              "offsetStart": "xs"
            }
          ]
        }
      }
    }
  ]
}

"""