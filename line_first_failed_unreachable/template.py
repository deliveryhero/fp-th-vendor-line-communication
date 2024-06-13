json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "อุปกรณ์ของคุณขาดการเชื่อมต่อ",
      "contents": {
        "type": "bubble",
        "size": "giga",
        "hero": {
          "type": "image",
          "url": "https://bucket.ex10.tech/images/f0fa557d-2258-11ef-a8d5-0242ac120003/originalContentUrl.jpg",
          "size": "full",
          "aspectRatio": "260:287",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": "https://tinyurl.com/AutoCommsytHTfgdga"
          }
        }
      }
    }
  ],
  "customAggregationUnits": [
    "LoseConnection"
  ]
}

"""