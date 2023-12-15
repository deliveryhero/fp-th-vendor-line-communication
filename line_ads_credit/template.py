json_object = """
{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "คุณกำลังมองหาวิธีเพิ่มยอดขายอยู่หรือไม่?",
      "contents": {
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://drive.google.com/uc?export=view&id=1WBthqM_JLFiDYC4Px1nUPZCy9xCRGcNl",
          "align": "center",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "20:20",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": "https://bit.ly/46fbhCt"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "position": "relative",
          "backgroundColor": "#F7C6CCFF",
          "borderColor": "#F7C6CC",
          "contents": [
            {
              "type": "text",
              "text": "เรียน ร้าน {vendor_name}",
              "align": "start",
              "wrap": true,
              "contents": [
                {
                  "type": "span",
                  "text": "เรียน ร้าน ",
                  "weight": "bold"
                },
                {
                  "type": "span",
                  "text": "{vendor_name}",
                  "weight": "regular"
                }
              ]
            },
            {
              "type": "text",
              "text": "รหัส {vendor_code}",
              "wrap": true,
              "contents": [
                {
                  "type": "span",
                  "text": "รหัส ",
                  "weight": "bold"
                },
                {
                  "type": "span",
                  "text": "{vendor_code}",
                  "weight": "regular"
                }
              ]
            },
            {
              "type": "separator",
              "margin": "lg",
              "color": "#F7C6CC"
            },
            {
              "type": "text",
              "text": "เพื่อประสิทธิภาพในการใช้งาน pandaclicks เราขอแนะนำให้คุณสมัคร ด้วยงบประมาณ: {recommended_budget} บาท",
              "align": "start",
              "wrap": true,
              "contents": []
            },
            {
              "type": "separator",
              "margin": "lg",
              "color": "#F7C6CC"
            },
            {
              "type": "text",
              "text": "ลองเลย! แล้วคุณจะเพลิดเพลินกับสิทธิประโยชน์มากมาย พร้อมส่วนลดพิเศษ 1,200 บาทเฉพาะคุณเท่านั้น!",
              "align": "start",
              "wrap": true,
              "position": "relative",
              "contents": []
            },
            {
              "type": "separator",
              "margin": "lg",
              "color": "#F7C6CC"
            },
            {
              "type": "text",
              "text": "ส่วนลดใช้งานอย่างไร👀",
              "wrap": true,
              "contents": []
            },
            {
              "type": "separator",
              "margin": "sm",
              "color": "#F7C6CC"
            },
            {
              "type": "text",
              "text": "- คุณจะได้รับส่วนลดเมื่อคุณสมัคร pandaclicks ในเดือนนี้เท่านั้น",
              "size": "xxs",
              "wrap": true,
              "contents": []
            },
            {
              "type": "text",
              "text": "- งบประมาณขั้นต่ำในการสมัคร pandaclicks คือ 2,250 บาท",
              "size": "xxs",
              "wrap": true,
              "contents": []
            },
            {
              "type": "text",
              "text": "- ส่วนลดสูงสุดที่คุณจะได้รับ คือ 1,200 บาท ",
              "size": "xxs",
              "wrap": true,
              "contents": []
            },
            {
              "type": "separator",
              "margin": "lg",
              "color": "#F7C6CC"
            },
            {
              "type": "text",
              "text": "ดูขั้นตอนการสมัคร pandaclicks คลิกที่นี่",
              "wrap": true,
              "action": {
                "type": "uri",
                "label": "คลิกที่นี่",
                "uri": "https://drive.google.com/file/d/1Cy_TchPsLdqEIuPj1SAHtplzLBwcCsTs/view?usp=sharing"
              },
              "contents": [
                {
                  "type": "span",
                  "text": "ดูขั้นตอนการสมัคร pandaclicks "
                },
                {
                  "type": "span",
                  "text": "คลิกที่นี่",
                  "color": "#FF2B85FF",
                  "decoration": "underline"
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "backgroundColor": "#F7C6CC",
          "borderColor": "#F7C6CC",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "สมัครเลย!",
                "uri": "https://bit.ly/46fbhCt"
              },
              "color": "#FF2B85FF",
              "style": "primary"
            }
          ]
        }
      }
    }
  ],
  "customAggregationUnits": [
    "AdCredits"
  ]
}

"""