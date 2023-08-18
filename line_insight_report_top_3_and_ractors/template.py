json_object = """
{
    "to": "{lineuserid}",
    "messages": [
        {
            "type": "flex",
            "altText": "เผย 3 อันดับ ร้านอาหารที่ลูกค้าสั่งซื้อมากสุด ดูเล้ย",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://drive.google.com/uc?export=view&id=1ToMHz6i0EJjQGstE_-CELZEPFtKUrkU1",
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
            "text": "หมายเหตุ: รายงานฉบับนี้อ้างอิงจากข้อมูลบนแพลตฟอร์ม foodpanda ในระยะ 1 เดือนย้อนหลังเท่านั้น",
            "size": "xs",
            "margin": "none",
            "wrap": true,
            "contents": [
              {
                "type": "span",
                "text": "สวัสดี!",
                "size": "sm"
              },
              {
                "type": "span",
                "text": " ร้าน {vendor_name}",
                "size": "md"
              }
            ]
          },
          {
            "type": "text",
            "text": "นี่คือร้านขายดี 3 อันดับแรกในพื้นที่การจัดส่งโซน {zone_name} ในหมวดหมู่ {cuisine_type}",
            "size": "sm",
            "wrap": true
          }
        ]
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
                "type": "image",
                "url": "https://drive.google.com/uc?export=view&id=1j0bLOo8SpQxODlvErxnTgSBJZHyv1N0k",
                "size": "full",
                "aspectMode": "fit",
                "offsetTop": "none",
                "offsetBottom": "none",
                "offsetStart": "xs",
                "align": "start",
                "gravity": "top",
                "position": "relative",
                "aspectRatio": "20:13"
              },
              {
                "type": "text",
                "text": "{custom_1}",
                "align": "center",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "gravity": "center",
                "weight": "bold",
                "size": "sm"
              }
            ],
            "flex": 2,
            "justifyContent": "flex-start"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "separator",
                "color": "#ffffff",
                "margin": "xl"
              },
              {
                "type": "image",
                "url": "https://drive.google.com/uc?export=view&id=18fYba89ixYx5EhBtrD3jtVCJrlKr79SI",
                "size": "full",
                "aspectRatio": "20:13"
              },
              {
                "type": "text",
                "text": "{custom_2}",
                "align": "center",
                "gravity": "center",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "weight": "bold",
                "size": "sm"
              }
            ],
            "flex": 2,
            "justifyContent": "flex-end"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://drive.google.com/uc?export=view&id=1dMYAFrUVzWT_lROGD_uYc0aVHGpMbWe9",
                "size": "full",
                "aspectRatio": "20:13"
              },
              {
                "type": "text",
                "text": "{custom_3}",
                "align": "center",
                "gravity": "top",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "weight": "bold",
                "size": "sm"
              },
              {
                "type": "separator",
                "margin": "xxl",
                "color": "#ffffff"
              }
            ],
            "flex": 2,
            "justifyContent": "flex-end"
          }
        ],
        "justifyContent": "center"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "separator",
        "margin": "md",
        "color": "#ffffff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "align": "center",
            "size": "sm",
            "contents": [
              {
                "type": "span",
                "text": "รู้หรือไม่?!",
                "color": "#FF2B85",
                "style": "italic",
                "weight": "bold",
                "decoration": "underline"
              },
              {
                "type": "span",
                "text": " ร้านอาหารที่มีคำสั่งซื้อมากที่สุด ในพื้นที่ของคุณ มีประสิทธิภาพในตัวชี้วัดเหล่านี้ที่ทำให้ลูกค้าตัดสินใจสั่งซื้อ",
                "size": "sm",
                "decoration": "none"
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#ffffff"
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
                "text": "ตัวชี้วัดที่ทำให้ลูกค้าตัดสินใจสั่งซื้อ",
                "wrap": true,
                "align": "center",
                "gravity": "center",
                "adjustMode": "shrink-to-fit",
                "size": "sm"
              }
            ],
            "flex": 2,
            "cornerRadius": "xxl",
            "backgroundColor": "#FFD271",
            "margin": "xs",
            "spacing": "xs",
            "justifyContent": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ข้อมูลร้านที่มีคำสั่งซื้อมากสุดในพื้นที่เดียวกับคุณ",
                "wrap": true,
                "gravity": "center",
                "adjustMode": "shrink-to-fit",
                "size": "xs",
                "margin": "xs",
                "align": "center"
              }
            ],
            "flex": 1,
            "backgroundColor": "#FFD271",
            "cornerRadius": "xxl",
            "spacing": "xs",
            "margin": "xs",
            "justifyContent": "center",
            "height": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ข้อมูลของร้านคุณ",
                "align": "center",
                "gravity": "center",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "size": "xs"
              }
            ],
            "flex": 1,
            "backgroundColor": "#FFD271",
            "cornerRadius": "xxl",
            "spacing": "xs",
            "margin": "xs",
            "justifyContent": "center"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md",
        "color": "#ffffff"
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
                "text": "จำนวนคำอธิบายเมนู",
                "size": "xs"
              }
            ],
            "flex": 2,
            "backgroundColor": "#FFD271",
            "cornerRadius": "xxl",
            "height": "30px",
            "justifyContent": "center",
            "alignItems": "center"
          },
          {
            "type": "text",
            "text": "{top_dld}%",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
          },
          {
            "type": "text",
            "text": "{vd_dld}%",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xs",
        "color": "#ffffff"
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
                "size": "xs",
                "text": "จำนวนรูปภาพเมนู"
              }
            ],
            "flex": 2,
            "backgroundColor": "#FFD271",
            "cornerRadius": "xxl",
            "height": "30px",
            "justifyContent": "center",
            "alignItems": "center"
          },
          {
            "type": "text",
            "text": "{top_dlp}%",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
          },
          {
            "type": "text",
            "text": "{vd_dlp}%",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xs",
        "color": "#ffffff"
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
                "text": "อัตราการปฏิเสธออเดอร์",
                "size": "xs"
              }
            ],
            "flex": 2,
            "backgroundColor": "#FFD271",
            "cornerRadius": "xxl",
            "height": "30px",
            "justifyContent": "center",
            "alignItems": "center"
          },
          {
            "type": "text",
            "text": "{top_failed_rate}%",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
          },
          {
            "type": "text",
            "text": "{vd_failed_rate}%",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xs",
        "color": "#ffffff"
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
                "text": "อัตราการปิดร้าน",
                "size": "xs"
              }
            ],
            "flex": 2,
            "backgroundColor": "#FFD271",
            "cornerRadius": "xxl",
            "height": "30px",
            "justifyContent": "center",
            "alignItems": "center"
          },
          {
            "type": "text",
            "text": "{top_offline}%",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
          },
          {
            "type": "text",
            "text": "{vd_offline}%",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xs",
        "color": "#ffffff"
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
                "text": "คะแนนเฉลี่ย",
                "size": "xs",
                "align": "start"
              }
            ],
            "flex": 2,
            "backgroundColor": "#FFD271",
            "cornerRadius": "xxl",
            "height": "30px",
            "justifyContent": "center",
            "alignItems": "center",
            "spacing": "none",
            "margin": "none"
          },
          {
            "type": "text",
            "text": "{top_rating}",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
          },
          {
            "type": "text",
            "text": "{vd_rating}",
            "flex": 1,
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "adjustMode": "shrink-to-fit",
            "size": "xs"
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
            "size": "xs",
            "margin": "sm",
            "wrap": true
          },
          {
            "type": "text",
            "text": "หากต้องการแจ้งปัญหาเกี่ยวกับรายงานฉบับนี้ คลิก ที่นี่!",
            "size": "xs",
            "margin": "none",
            "wrap": true,
            "color": "#FF2B85",
            "adjustMode": "shrink-to-fit",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://forms.gle/mvui56d7yn53HfHy6"
            }
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
          "label": "อ่านทริคเพิ่มเติม>",
          "uri": "https://bit.ly/45mWC7m"
        },
        "color": "#FF2B85",
        "height": "sm",
        "position": "relative",
        "margin": "none",
        "style": "primary",
        "offsetTop": "xs",
        "offsetBottom": "xs",
        "offsetStart": "xs",
        "offsetEnd": "xs"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "จัดการร้านเลย >",
          "uri": "https://bit.ly/3pAh8Ce"
        },
        "color": "#FF2B85",
        "height": "sm",
        "position": "relative",
        "margin": "sm",
        "style": "primary",
        "offsetTop": "xs",
        "offsetBottom": "xs",
        "offsetStart": "xs",
        "offsetEnd": "xs"
      }
    ],
    "backgroundColor": "#FFFFFF",
    "spacing": "none",
    "margin": "none",
    "borderColor": "#FFFFFF",
    "borderWidth": "none"
  }
}

    }
  ]
}
"""