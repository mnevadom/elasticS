import aws_api.api_client
import pprint
import boto3
import os
import aws_lambda.zip_my_file
#import aws_lambda.lambda_ex
import aws_lambda.lambda_client
import aws_api

client = boto3.client('apigateway')

#pprint.pprint(api_client.get_method('wrie62gtmd', 'v35hj3', 'GET'))

#pprint.pprint(api_client.put_integration_method('wrie62gtmd', '5s1ftd', 'POST', uriLambdaFunc))
#pprint.pprint(api_client.create_resource('wrie62gtmd', 'v35hj3', 'pruebares'))
#resMethod = api_client.put_resource_method('wrie62gtmd', 'v35hj3', 'GET', '')

#resIntegr = api_client.put_integration_method('wrie62gtmd', 'v35hj3', 'GET', uriLambdaFunc)
#filename = os.path.join('aws_lambda', 'get_container_func.zip')
#print(filename)
#print(aws_lambda.zip_my_file.create_zip_file(os.path.abspath('../aws_lambda/get_container_func.py')))

# need to get the uri of aws_lambda function, for now: arn:aws:apigateway:us-east-1:aws_lambda:path/2015-03-31/functions/arn:aws:aws_lambda:us-east-1:471454180135:function:getContainer/invocations
# uriLambdaFunc = 'arn:aws:apigateway:us-east-1:aws_lambda:path/2015-03-31/functions/arn:aws:aws_lambda:us-east-1:471454180135:function:getContainer/invocations'

#print(aws_lambda.lambda_ex.create_lambda_function2('/Users/marionevado/PycharmProjects/phiAws/aws_lambda/get_container_func.zip', 'pruebasFun',
 #                                                  'arn:aws:iam::471454180135:role/lambda_dynamo', 'get_container_func.lambda_handler'))

#pprint.pprint(aws_lambda.lambda_client.get_function('pruebasFun'))

#pprint.pprint(aws_api.api_client.get_rest_apis())
#pprint.pprint(aws_api.api_client.get_resources('uv20wv3ee9', 3))
pprint.pprint(aws_api.api_client.get_integration_method('uv20wv3ee9', 'qidxa8', 'GET'))

#aws_api.api_controller.delete_api('PhiApiName')

#aws_api.api_client.delete_rest_api('qm77br0bw0')