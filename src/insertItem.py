import json
import boto3
from uuid import uuid4

def insert_item(event):
    body = json.loads(event['body'])
    item = body['item']
    created_at = datetime.datetime.now().isoformat()
    item_id = str(uuid4())

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ItemTable')

    new_item = {
        'id': item_id,
        'item': item,
        'createdAt': created_at,
        'itemStatus': False
    }

    table.put_item(Item=new_item)

    return {
        'statusCode': 200,
        'body': json.dumps(new_item)
    }

def lambda_handler(event, context):
    return insert_item(event)
