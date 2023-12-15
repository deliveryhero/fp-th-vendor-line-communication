json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "จัดการธุรกิจอย่างมีประสิทธิภาพด้วยพอร์ทัลร้านอาหาร",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://drive.google.com/uc?export=view&id=1bfjWwwsp8MpbbH6TvIchVpyXUSCdrZWp",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "100:100",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "คลิก",
            "uri": "http://bit.ly/40kTIxZ"
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
                "label": "ทำความรู้จักเครื่องมือ",
                "uri": "https://youtube.com/playlist?list=PLWLrh3ZaezZxa9YqmqTYBbTSn9iKrwx6m&si=zJFMlNXUPOzbCsBd"
              },
              "color": "#FF2B85FF",
              "style": "primary",
              "height": "sm",
              "offsetTop": "none",
              "offsetStart": "none",
              "offsetEnd": "xs"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ดูวิธีเข้าใช้งาน",
                "uri": "https://bit.ly/3lL6yXc"
              },
              "color": "#FF2B85FF",
              "height": "sm",
              "style": "primary",
              "offsetEnd": "none",
              "offsetStart": "xs"
            }
          ],
          "backgroundColor": "#F7C6CC"
        }
      }
    }
  ]
}

"""