import boto3


def lambda_handler(event, context):
    #client = boto3.client('dynamodb')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('container')
    
    response = table.get_item(
        Key={
            'id': event['id']
        }
    )
    
    item = response['Item']
    print(item)
    return item