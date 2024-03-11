json_object_success = """

{
    "to": "{line_user_id}",
    "messages": [
        {
            "type": "flex",
            "altText": "ผูกไลน์สำเร็จแล้ว!",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://bucket.ex10.tech/images/b133db2a-d5f7-11ee-97d4-0242ac12000b/originalContentUrl.jpg",
    "size": "full",
    "aspectRatio": "4:4",
    "aspectMode": "cover"
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
    "to": "{line_user_id}",
    "messages": [
        {
            "type": "flex",
            "altText": "ผูกไลน์ไม่สำเร็จ!",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://bucket.ex10.tech/images/ec46337f-d5f5-11ee-97d4-0242ac12000b/originalContentUrl.jpg",
    "size": "full",
    "aspectRatio": "4:4",
    "aspectMode": "cover"
  }
}
    }
  ],
    "customAggregationUnits": [
        "notsuccessfulveri"]
}

"""