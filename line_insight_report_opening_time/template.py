json_object = """
{
    "to": "{lineuserid}",
    "messages": [
        {
            "type": "flex",
            "altText": "ตรวจสอบช่วงมื้ออาหารที่ขายดีของร้านคุณและคู่แข่ง!",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://drive.google.com/uc?export=view&id=1h1dKtRjR3QmfxcdtL5fCmNpDkZctxcVU",
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
            "type": "text",
            "text": "สวัสดี!",
            "contents": [
              {
                "type": "span",
                "text": "สวัสดี!",
                "size": "sm"
              },
              {
                "type": "span",
                "text": " ร้าน {vendor_name}",
                "size": "sm"
              }
            ]
          },
          {
            "type": "text",
            "text": "ตรวจสอบช่วงมื้ออาหารที่ขายดีบนแพลตฟอร์มเรา! ในพื้นที่การจัดส่งโซน {zone_name}",
            "wrap": true,
            "size": "sm"
          }
        ]
      },
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
                "text": "แสดงข้อมูลคำสั่งซื้อของร้านในพื้นที่เดียวกับคุณ",
                "size": "sm",
                "margin": "none",
                "weight": "bold",
                "style": "italic",
                "decoration": "underline"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "cornerRadius": "xxl",
            "backgroundColor": "#FF2B85",
            "height": "15px",
            "width": "50px",
            "justifyContent": "center",
            "alignItems": "center",
            "spacing": "xs",
            "margin": "none"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "แสดงข้อมูลคำสั่งซื้อของร้านคุณ",
            "size": "sm",
            "style": "italic",
            "decoration": "underline",
            "margin": "sm",
            "weight": "bold"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "cornerRadius": "xxl",
            "backgroundColor": "#FFD271",
            "height": "15px",
            "width": "50px",
            "justifyContent": "center",
            "alignItems": "center",
            "spacing": "none",
            "margin": "none"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "5AM  - 10AM (มื้อเช้า)",
            "margin": "xs",
            "size": "sm"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FF2B85",
                "height": "15px",
                "width": "{custome_11}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "xs",
            "margin": "xs"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FFD271",
                "height": "15px",
                "width": "{custome_1}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "none",
            "margin": "none"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "10AM  - 2PM (มื้อกลางวัน)",
            "margin": "sm",
            "size": "sm"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FF2B85",
                "height": "15px",
                "width": "{custome_22}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "xs",
            "margin": "xs"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FFD271",
                "height": "15px",
                "width": "{custome_2}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "none",
            "margin": "none"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "2PM  - 5PM (มื้อบ่าย)",
            "margin": "sm",
            "size": "sm"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": []
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FF2B85",
                "height": "15px",
                "width": "{custome_33}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "xs",
            "margin": "xs"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FFD271",
                "height": "15px",
                "width": "{custome_3}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "none",
            "margin": "none"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "5PM  - 10PM (มื้อเย็น)",
            "margin": "sm",
            "size": "sm"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FF2B85",
                "height": "15px",
                "width": "{custome_44}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "xs",
            "margin": "xs"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FFD271",
                "height": "15px",
                "width": "{custome_4}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "none",
            "margin": "none"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "10PM - 5AM (มื้อดึก)",
            "margin": "sm",
            "size": "sm"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FF2B85",
                "height": "15px",
                "width": "{custome_55}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "xs",
            "margin": "xs"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "cornerRadius": "xxl",
                "backgroundColor": "#FFD271",
                "height": "15px",
                "width": "{custome_5}px",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none",
                "margin": "none"
              }
            ],
            "spacing": "none",
            "margin": "none"
          }
        ]
      },
      {
        "type": "text",
        "text": "*หากไม่มีข้อมูลในช่วงมื้ออาหารนั้นๆ กราฟแท่งจะไม่แสดงสี",
        "wrap": true,
        "size": "sm",
        "margin": "md"
      },
      {
        "type": "text",
        "text": "หมายเหตุ: รายงานฉบับนี้อ้างอิงจากข้อมูลบนแพลตฟอร์ม foodpanda ในระยะ 1 เดือนย้อนหลังเท่านั้น",
        "wrap": true,
        "size": "sm",
        "margin": "md"
      }
    ],
    "justifyContent": "flex-start",
    "alignItems": "flex-start",
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
          "label": "ปรับเวลาทำการเพื่อให้ได้คำสั่งซื้อที่เพิ่มขึ้น >",
          "uri": "https://bit.ly/3ril0Zj"
        },
        "color": "#FFFFFF",
        "height": "sm"
      }
    ],
    "backgroundColor": "#FF2B85"
  }
}

    }
  ]
}
"""