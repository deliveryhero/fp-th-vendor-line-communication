json_object = """
{
    "to": "{lineuserid}",
    "messages": [
        {
            "type": "flex",
            "altText": "ดูเล้ย 5 อันดับประเภทอาหารขายดี! ในพื้นที่ของคุณ",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://drive.google.com/uc?export=view&id=1ABRkd0zeTBuPdNhXI-fEOQniHBo6SvTm",
    "size": "full",
    "aspectRatio": "20:10",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "สวัสดี! ร้าน",
                "contents": [
                  {
                    "type": "span",
                    "text": "สวัสดี! ร้าน",
                    "style": "normal",
                    "weight": "bold"
                  },
                  {
                    "type": "span",
                    "text": " {vendor_name}"
                  }
                ]
              },
              {
                "type": "text",
                "text": "นี่คือ 5 อันดับประเภทอาหารที่ขายดีในบริเวณโซนพื้นที่ {zone_name}",
                "wrap": true
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "1.  {menu1}",
                "color": "#FF2B85",
                "size": "lg",
                "gravity": "center",
                "align": "start",
                "wrap": true,
                "adjustMode": "shrink-to-fit"
              },
              {
                "type": "text",
                "text": "{menu1_percent}%",
                "color": "#FF2B85",
                "align": "center",
                "size": "lg",
                "gravity": "center",
                "margin": "lg",
                "wrap": true,
                "adjustMode": "shrink-to-fit"
              }
            ],
            "paddingTop": "2px",
            "paddingAll": "12px",
            "paddingBottom": "2px",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "2. {menu2}",
                "color": "#FF2B85",
                "size": "lg",
                "gravity": "center",
                "align": "start",
                "wrap": true,
                "adjustMode": "shrink-to-fit"
              },
              {
                "type": "text",
                "text": "{menu2_percent}%",
                "color": "#FF2B85",
                "align": "center",
                "size": "lg",
                "gravity": "center",
                "margin": "lg",
                "wrap": true,
                "adjustMode": "shrink-to-fit"
              }
            ],
            "paddingTop": "2px",
            "paddingAll": "12px",
            "paddingBottom": "2px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "3. {menu3}",
                "color": "#FF2B85",
                "size": "lg",
                "gravity": "center",
                "align": "start",
                "wrap": true,
                "adjustMode": "shrink-to-fit"
              },
              {
                "type": "text",
                "text": "{menu3_percent}%",
                "color": "#FF2B85",
                "align": "center",
                "size": "lg",
                "gravity": "center",
                "margin": "lg",
                "wrap": true,
                "adjustMode": "shrink-to-fit"
              }
            ],
            "paddingTop": "2px",
            "paddingAll": "12px",
            "paddingBottom": "2px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "4. {menu4}",
                "size": "lg",
                "gravity": "center",
                "align": "start",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "color": "#FF2B85"
              },
              {
                "type": "text",
                "text": "{menu4_percent}%",
                "gravity": "center",
                "align": "center",
                "size": "lg",
                "margin": "lg",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "color": "#FF2B85"
              }
            ],
            "paddingAll": "12px",
            "paddingTop": "2px",
            "paddingBottom": "2px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "5. {menu5}",
                "size": "lg",
                "gravity": "center",
                "align": "start",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "color": "#FF2B85"
              },
              {
                "type": "text",
                "text": "{menu5_percent}%",
                "gravity": "center",
                "align": "center",
                "size": "lg",
                "margin": "lg",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "color": "#FF2B85"
              }
            ],
            "paddingAll": "12px",
            "paddingTop": "2px",
            "paddingBottom": "2px",
            "margin": "none",
            "spacing": "none"
          }
        ],
        "margin": "sm",
        "backgroundColor": "#EFF2F4"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "👀 เมนูอาหารที่มีรูปที่น่ารับประทาน สามารถเพิ่มยอดขายได้เฉลี่ยถึง 10% ",
                "flex": 2,
                "size": "md",
                "gravity": "center",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "weight": "regular"
              },
              {
                "type": "image",
                "url": "https://drive.google.com/uc?export=view&id=1_kOogpU_-Tdn5yTI8_q7ddlIOalkRsag",
                "flex": 1,
                "position": "relative"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "หมายเหตุ: รายงานฉบับนี้อ้างอิงจากข้อมูลบนแพลตฟอร์ม foodpanda ในระยะ 1 เดือนย้อนหลังเท่านั้น",
                "adjustMode": "shrink-to-fit",
                "wrap": true,
                "size": "xs"
              }
            ],
            "spacing": "lg",
            "margin": "lg"
          }
        ],
        "spacing": "lg",
        "backgroundColor": "#EFF2F4",
        "margin": "lg"
      }
    ],
    "paddingAll": "10px",
    "backgroundColor": "#EFF2F4"
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
          "uri": "https://bit.ly/3pEyDBx"
        },
        "color": "#FFFFFF",
        "height": "sm"
      }
    ],
    "backgroundColor": "#FF2B85",
    "spacing": "none",
    "margin": "none"
  },
  "styles": {
    "footer": {
      "backgroundColor": "#EFF2F4"
    }
  }
}
    }
  ]
}
"""