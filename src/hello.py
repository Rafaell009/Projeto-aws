import json

def hello(event):
    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'message': 'Go Serverless v2.0! Your function executed successfully!',
                'input': event
            },
            indent=2
        )
    }

def lambda_handler(event, context):
    return hello(event)
