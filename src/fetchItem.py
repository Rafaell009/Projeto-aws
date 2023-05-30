import boto3

def fetch_item(event):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ItemTable')

    id = event['pathParameters']['id']

    try:
        response = table.get_item(Key={'id': id})
        item = response['Item']
    except Exception as e:
        print(e)
        item = None

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def lambda_handler(event, context):
    return fetch_item(event)
