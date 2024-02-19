json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "ร้านของคุณออฟไลน์บนระบบในวันที่ผ่านมา",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "hero": {
          "type": "image",
          "size": "full",
          "aspectRatio": "1040:1800",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": "https://foodpanda.portal.restaurant/opening-times-pandora"
          },
          "url": "https://bucket.ex10.tech/images/50e27b29-c5a7-11ee-97d4-0242ac12000b/originalContentUrl.jpg"
        }
      }
    }
  ],
  "customAggregationUnits": [
    "Unreachabletablet"
  ]
}

"""