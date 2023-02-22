json_object = """
{
    "to": "{line_user_id}",
    "messages": [
        {
            "type": "flex",
            "altText": "ร้านของคุณมีเวลาออฟไลน์ เนื่องจากเช็กอินล่าช้ากว่าเวลาทำการบนระบบ",
            "contents":
{
  "type": "bubble",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://drive.google.com/uc?export=view&id=1t-_pm0agkInZxubSfHTv_pCyRsGxKNkc",
    "size": "full",
    "aspectRatio": "4:4",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://bit.ly/3RM70Ae"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ร้านของคุณมีเวลาออฟไลน์ เนื่องจากเช็กอินล่าช้ากว่าเวลาทำการบนระบบ ใน 7 วันที่ผ่านมา เป็นเวลา {sum_check_in_required_mins}",
        "align": "start",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "ร้านของคุณมีเวลาออฟไลน์ เนื่องจากเช็กอินล่าช้ากว่าเวลาทำการบนระบบ ใน 7 วันที่ผ่านมา "
          },
          {
            "type": "span",
            "text": "เป็นเวลา {sum_check_in_required_mins}",
            "color": "#FF2B85FF",
            "weight": "bold"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#FFFFFFFF"
      },
      {
        "type": "text",
        "text": "หรือถ้าคุณไม่ได้เปิดร้านในเวลาดังกล่าว เราขอแนะนำให้คุณเปลี่ยนเวลาทำการบนพอร์ทัลร้านอาหารให้ตรงกับเวลาทำการหน้าร้านหรือหากหยุดร้าน ให้ตั้งค่าวันหยุดและช่วงเวลาทำการพิเศษ ดูวิธีการทำ คลิก!",
        "wrap": true,
        "action": {
          "type": "uri",
          "label": "ดูวิธีการทำ คลิก!",
          "uri": "http://bit.ly/3YIbw4W"
        },
        "contents": [
          {
            "type": "span",
            "text": "หรือถ้าคุณไม่ได้เปิดร้านในเวลาดังกล่าว เราขอแนะนำให้คุณเปลี่ยนเวลาทำการบนพอร์ทัลร้านอาหารให้ตรงกับเวลาทำการหน้าร้านหรือหากหยุดร้าน ให้ตั้งค่าวันหยุดและช่วงเวลาทำการพิเศษ"
          },
          {
            "type": "span",
            "text": "ดูวิธีการทำ คลิก!",
            "color": "#FF2B85FF",
            "weight": "bold",
            "decoration": "underline"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "เปลี่ยนเวลาทำการเลย!",
          "uri": "http://bit.ly/3RM70Ae"
        },
        "color": "#FF2B85FF",
        "style": "primary"
      }
    ]
  }
}
    }
  ]
}
"""