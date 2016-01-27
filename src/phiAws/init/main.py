import aws_api.api_client
import aws_lambda.lambda_client
import help
import aws_dynamodb.dynamo_client

print('Creating dynamoDb table: container...')
aws_dynamodb.dynamo_client.create_table_container()

print('Creating zip file to upload lambda function...')
#help.zip_create
#zipdata

print('uploading lambda function... ')
#aws_lambda.lambda_client.create_function('creandofun', 'arn:aws:iam::471454180135:role/lambda_dynamo', 'get_container_func.lambda_handler', zipdata)

print('Creating ')