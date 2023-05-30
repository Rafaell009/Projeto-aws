import json
import boto3

def update_item(event):
    body = json.loads(event['body'])
    item_status = body['itemStatus']
    item_id = event['pathParameters']['id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ItemTable')

    table.update_item(
        Key={'id': item_id},
        UpdateExpression='set itemStatus = :itemStatus',
        ExpressionAttributeValues={':itemStatus': item_status},
        ReturnValues="ALL_NEW"
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'msg': 'Item updated'})
    }

def lambda_handler(event, context):
    return update_item(event)
