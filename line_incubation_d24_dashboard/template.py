json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "ดูภาพรวมออเดอร์และยอดขายได้ง่ายๆ",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://drive.google.com/uc?export=view&id=1UbTwFxXNEdsnRXYtNhdoSBRY8d9fiBkt",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "100:100",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "คลิก",
            "uri": "http://bit.ly/42MoAcf"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ทบทวนวิธีการใช้เครื่องมือบน panda partner ทั้งหมด คลิก!",
              "size": "sm",
              "style": "italic",
              "align": "center",
              "action": {
                "type": "uri",
                "label": "action",
                "uri": "https://youtube.com/playlist?list=PLWLrh3ZaezZxa9YqmqTYBbTSn9iKrwx6m&si=cc9oSKczWszGZPSd"
              }
            }
          ],
          "backgroundColor": "#FFFFFF",
          "cornerRadius": "lg",
          "paddingAll": "xs"
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