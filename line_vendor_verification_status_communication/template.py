json_object_success = """

{
    "to": "line_user_id",
    "messages": [
        {
            "type": "flex",
            "altText": "ผูกไลน์สำเร็จแล้ว!",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://bucket.ex10.tech/images/a7489bab-e01f-11ee-97d4-0242ac12000b/originalContentUrl.jpg",
    "align": "center",
    "gravity": "center",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "รหัสร้าน vendor_code ได้ผูกไลน์กับ foodpanda สำเร็จแล้ว",
        "align": "center",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "รหัสร้าน "
          },
          {
            "type": "span",
            "text": "vendor_code ",
            "color": "#FF2B85"
          },
          {
            "type": "span",
            "text": "ได้ผูกไลน์กับ foodpanda สำเร็จแล้ว"
          }
        ]
      }
    ]
  }
}
    }
  ],
    "customAggregationUnits": [
        "successfulveri"]
}

"""

json_object_not_success = """
{
    "to": "line_user_id",
    "messages": [
        {
            "type": "flex",
            "altText": "ผูกไลน์ไม่สำเร็จ!",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://bucket.ex10.tech/images/90768759-e01f-11ee-97d4-0242ac12000b/originalContentUrl.jpg",
    "align": "center",
    "gravity": "center",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "รหัสร้าน vendor_code ผูกไลน์กับ foodpanda ไม่สำเร็จ เนื่องจากรหัสร้านค้า หรือ เบอร์โทรศัพท์ที่กรอกมาไม่ถูกต้อง  กรุณาดำเนินการใหม่อีกครั้ง",
        "align": "center",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "รหัสร้าน "
          },
          {
            "type": "span",
            "text": "vendor_code ",
            "color": "#FF2B85"
          },
          {
            "type": "span",
            "text": "ผูกไลน์กับ foodpanda ไม่สำเร็จ เนื่องจากรหัสร้านค้า หรือ เบอร์โทรศัพท์ที่กรอกมาไม่ถูกต้อง  กรุณาดำเนินการใหม่อีกครั้ง"
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
          "label": "ผูกไลน์อีกครั้ง คลิก",
          "uri": "https://liff.line.me/1657390248-5lAWzgRz"
        },
        "color": "#FF2B85",
        "height": "sm",
        "style": "primary"
      }
    ]
  }
}
    }
  ],
    "customAggregationUnits": [
        "notsuccessfulveri"]
}

"""