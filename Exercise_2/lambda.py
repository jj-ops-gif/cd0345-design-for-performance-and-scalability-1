import json

def lambda_handler(event, context):
    print('Hello Udacity!')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
