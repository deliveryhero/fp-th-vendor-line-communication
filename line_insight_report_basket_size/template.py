json_object = """
{
    "to": "{lineuserid}",
    "messages": [
        {
            "type": "flex",
            "altText": "อยากรู้มั้ย? ลูกค้าสั่งซื้ออาหารต่อครั้งเท่าไหร่??",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://drive.google.com/uc?export=view&id=1Pjh20vQsKWCsVFSz643qw9ltyRKSsyMo",
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
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "size": "xs",
            "gravity": "center",
            "wrap": true,
            "align": "start",
            "adjustMode": "shrink-to-fit",
            "margin": "lg",
            "contents": [
              {
                "type": "span",
                "text": "สวัสดี!",
                "size": "md"
              },
              {
                "type": "span",
                "text": " ร้าน {vendor_name}",
                "size": "md"
              }
            ]
          }
        ],
        "margin": "none"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "นี่คือข้อมูลสถิติของมูลค่าการสั่งซื้ออาหารต่อครั้งของร้านคุณ และร้านทั้งหมดที่อยู่ในบริเวณโซนพื้นที่ {zone_name}",
            "size": "sm",
            "gravity": "center",
            "wrap": true,
            "align": "start",
            "adjustMode": "shrink-to-fit",
            "margin": "lg"
          }
        ],
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://drive.google.com/uc?export=view&id=12vbX-x6q1YsCp586a-XgxI5mcSLoF1J9",
            "aspectMode": "fit",
            "margin": "none",
            "size": "3xl",
            "flex": 2,
            "aspectRatio": "20:10"
          },
          {
            "type": "image",
            "url": "https://drive.google.com/uc?export=view&id=1GfJFi82mmk5S-Eg-XWT3fCGvLJf7QqPX",
            "size": "3xl",
            "gravity": "center",
            "align": "end",
            "flex": 1,
            "aspectMode": "fit"
          },
          {
            "type": "image",
            "url": "https://drive.google.com/uc?export=view&id=15EW5Owd5c5qST2om_vG1oXOCFq_4yPor",
            "size": "4xl",
            "flex": 1,
            "aspectMode": "fit"
          }
        ],
        "alignItems": "center",
        "backgroundColor": "#EFF2F4",
        "spacing": "none",
        "margin": "md"
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
                "type": "image",
                "url": "https://drive.google.com/uc?export=view&id=1aF2C31IbqS7H8wKM4eelf5oSC6W6fLlS",
                "size": "lg",
                "aspectMode": "fit",
                "flex": 2,
                "aspectRatio": "20:8",
                "backgroundColor": "#EFF2F4"
              },
              {
                "type": "text",
                "text": "{custome_Zone_1}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              },
              {
                "type": "text",
                "text": "{custome_1}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              }
            ],
            "spacing": "none",
            "margin": "none",
            "position": "relative",
            "borderColor": "#FFD271",
            "backgroundColor": "#EFF2F4",
            "height": "50px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://drive.google.com/uc?export=view&id=1pNoXS_6LEDb3QEFUQsmWHdYaZIyyWmCD",
                "size": "lg",
                "aspectMode": "fit",
                "flex": 2,
                "aspectRatio": "20:8"
              },
              {
                "type": "text",
                "text": "{custome_Zone_2}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              },
              {
                "type": "text",
                "text": "{custome_2}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              }
            ],
            "spacing": "none",
            "margin": "none",
            "backgroundColor": "#EFF2F4",
            "height": "50px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://drive.google.com/uc?export=view&id=1ZPpkpEMmZY5SqhwCCfCIq4eH9XmAM_JC",
                "size": "lg",
                "flex": 2,
                "aspectRatio": "20:8"
              },
              {
                "type": "text",
                "text": "{custome_Zone_3}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              },
              {
                "type": "text",
                "text": "{custome_3}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              }
            ],
            "backgroundColor": "#EFF2F4",
            "height": "50px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://drive.google.com/uc?export=view&id=1glO6Lmca0I6WZHv8Fc7vWvswtgafDtpH",
                "size": "lg",
                "flex": 2,
                "aspectRatio": "20:8"
              },
              {
                "type": "text",
                "text": "{custome_Zone_4}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              },
              {
                "type": "text",
                "text": "{custome_4}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              }
            ],
            "backgroundColor": "#EFF2F4",
            "height": "50px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://drive.google.com/uc?export=view&id=1NeC7raMH446o3kEupj-sYS77NbUhYN41",
                "size": "lg",
                "flex": 2,
                "aspectRatio": "20:8"
              },
              {
                "type": "text",
                "text": "{custome_Zone_5}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              },
              {
                "type": "text",
                "text": "{custome_5}%",
                "gravity": "center",
                "align": "center",
                "wrap": true,
                "size": "lg"
              }
            ],
            "backgroundColor": "#EFF2F4",
            "height": "50px"
          }
        ],
        "borderColor": "#EFF2F4"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "*หากข้อมูลแสดงค่าเท่ากับ 0 หมายความว่าไม่มีข้อมูลในช่วงมูลค่าการสั่งซื้อนั้นๆ",
            "size": "xs",
            "wrap": true
          },
          {
            "type": "text",
            "text": "หมายเหตุ: รายงานฉบับนี้อ้างอิงจากข้อมูลบนแพลตฟอร์ม foodpanda ในระยะ 1 เดือนย้อนหลังเท่านั้น",
            "size": "xs",
            "gravity": "center",
            "wrap": true,
            "align": "start",
            "adjustMode": "shrink-to-fit",
            "margin": "lg"
          }
        ],
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "หากต้องการแจ้งปัญหาเกี่ยวกับรายงานฉบับนี้ คลิก ที่นี่!",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://forms.gle/mvui56d7yn53HfHy6"
            },
            "size": "xs",
            "wrap": true,
            "color": "#FF2B85"
          }
        ],
        "margin": "none",
        "spacing": "none",
        "height": "20px",
        "borderColor": "#FF2B85",
        "justifyContent": "center",
        "alignItems": "center"
      }
    ],
    "backgroundColor": "#EFF2F4"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "uri": "https://bit.ly/451LxJb",
          "label": "อ่านทริคเพิ่มเติม>"
        },
        "color": "#FF2B85",
        "offsetTop": "xs",
        "offsetBottom": "xs",
        "offsetStart": "xs",
        "offsetEnd": "xs",
        "height": "sm",
        "margin": "none",
        "position": "relative",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "uri": "https://bit.ly/3NEh38E",
          "label": "ปรับปรุงเมนูเลย>"
        },
        "color": "#FF2B85",
        "offsetTop": "xs",
        "offsetBottom": "xs",
        "offsetStart": "xs",
        "offsetEnd": "xs",
        "height": "sm",
        "margin": "sm",
        "position": "relative",
        "style": "primary",
        "gravity": "top",
        "scaling": true,
        "adjustMode": "shrink-to-fit"
      }
    ],
    "backgroundColor": "#EFF2F4",
    "borderColor": "#FF2B85",
    "margin": "none",
    "spacing": "none"
  },
  "styles": {
    "header": {
      "separator": false
    }
  }
}
    }
  ]
}
"""