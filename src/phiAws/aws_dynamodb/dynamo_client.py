import boto3


def create_table_container():
    dynamodb = boto3.resource('aws_dynamodb')
    table = dynamodb.create_table(
            TableName='container',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'nombre',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'nombre',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='prBoto3')
    print ('table created: ')
    print(table.item_count)
