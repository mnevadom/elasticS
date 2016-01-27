import boto3

def lambda_handler(event, context):
    #client = boto3.client('aws_dynamodb')
    dynamodb = boto3.resource('aws_dynamodb')
    table = dynamodb.Table('container')

    response = table.get_item(
        Key={
            'id': event['id']
        }
    )

    item = response['Item']
    print(item)
    return item