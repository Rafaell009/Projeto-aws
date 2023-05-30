import boto3
import json

def fetch_items(event):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ItemTable')

    try:
        response = table.scan()
        items = response['Items']
    except Exception as e:
        print(e)
        items = []

    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }

def lambda_handler(event, context):
    return fetch_items(event)
