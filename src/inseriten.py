dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ItemTable")

newItem = {
    "id": id,
    "item": item,
    "createdAt": createdAt,
    "itemStatus": False
}

table.put_item(Item=newItem)

response = {
    "statusCode": 200,
    "body": json.dumps(newItem)
}

return response
