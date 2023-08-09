json_object = """
{
    "to": "{lineuserid}",
    "messages": [
        {
            "type": "flex",
            "altText": "5 เมนูที่ลูกค้าค้นหามากที่สุด ดูเล้ย",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "size": "full",
    "aspectRatio": "20:10",
    "aspectMode": "cover",
    "url": "https://drive.google.com/uc?export=view&id=1Aux3cLJX90cz40tO9xoKEcEmmI3KRrNk"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "size": "md",
            "wrap": true,
            "gravity": "center",
            "align": "start",
            "flex": 3,
            "adjustMode": "shrink-to-fit",
            "text": "hi",
            "contents": [
              {
                "type": "span",
                "text": "สวัสดี!"
              },
              {
                "type": "span",
                "text": " ร้าน {vendor_name}"
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": " 10 คีย์เวิร์ด",
            "size": "3xl",
            "contents": [
              {
                "type": "span",
                "text": "5 ประเภทอาหาร",
                "size": "xl",
                "color": "#FF2B85",
                "weight": "bold",
                "style": "italic",
                "decoration": "underline"
              },
              {
                "type": "span",
                "text": "ที่ลูกค้าค้นหาเพื่อสั่งซื้อมากที่สุดในบริเวณโซนพื้นที่ {zone_name}",
                "size": "md"
              }
            ],
            "adjustMode": "shrink-to-fit",
            "wrap": true,
            "align": "center",
            "position": "relative"
          }
        ],
        "spacing": "xxl",
        "margin": "xxl",
        "justifyContent": "flex-start",
        "cornerRadius": "xxl",
        "backgroundColor": "#FFD271"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "#1 {custome_1}",
            "size": "xxl",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "align": "start",
            "gravity": "center",
            "color": "#FF2B85"
          }
        ],
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "#2 {custome_2}",
            "size": "xl",
            "wrap": true,
            "gravity": "center",
            "adjustMode": "shrink-to-fit",
            "color": "#FF2B85",
            "align": "start"
          }
        ],
        "alignItems": "center"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "#3 {custome_3}",
                "flex": 2,
                "align": "start",
                "gravity": "top",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "size": "xl",
                "color": "#FF2B85"
              }
            ],
            "flex": 2
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "#4 {custome_4}",
            "size": "lg",
            "wrap": true,
            "gravity": "center",
            "align": "start",
            "flex": 3,
            "adjustMode": "shrink-to-fit"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "#5 {custome_5}",
            "size": "lg",
            "wrap": true,
            "gravity": "center",
            "align": "start",
            "flex": 3,
            "adjustMode": "shrink-to-fit"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "หมายเหตุ: รายงานฉบับนี้อ้างอิงจากข้อมูลบนแพลตฟอร์ม foodpanda ในระยะ 1 เดือนย้อนหลังเท่านั้น",
            "size": "xs",
            "margin": "md",
            "wrap": true
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "ร้านไหนยังไม่มีเพิ่มเลย>",
          "uri": "https://bit.ly/3O1DUwp"
        },
        "color": "#FFFFFF",
        "height": "sm",
        "style": "link"
      }
    ],
    "backgroundColor": "#FF2B85",
    "cornerRadius": "none",
    "borderWidth": "none"
  }
}

    }
  ]
}
"""