json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "สำคัญ! ป้องกันการเพิ่มอัตราการออฟไลน์ ควรทำอย่างไร?!",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://drive.google.com/uc?export=view&id=1UhYEovrEeNm7bc_ikdhfyWrHm_gXm-c5",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "100:100",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "คลิก",
            "uri": "http://bit.ly/3JPWVi2"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ดูวิธีการจัดการ panda partner ทั้งหมด  คลิก!",
              "style": "italic",
              "align": "center",
              "size": "xs",
              "action": {
                "type": "uri",
                "label": "action",
                "uri": "https://youtube.com/playlist?list=PLWLrh3ZaezZxa9YqmqTYBbTSn9iKrwx6m&si=cc9oSKczWszGZPSd"
              }
            }
          ],
          "cornerRadius": "lg",
          "backgroundColor": "#FFFFFF",
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