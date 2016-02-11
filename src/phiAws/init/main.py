import aws_api.api_client
import aws_lambda.lambda_ex
import aws_api.api_controller
import help
import aws_dynamodb.dynamo_client
import os
import pprint

aws_api.api_controller.delete_rest_api('PhiApiName')

print('Creating dynamoDb table: container...')
#aws_dynamodb.dynamo_client.create_table_container()

print('Creating rest api...')
idApi = aws_api.api_controller.create_api('PhiApiName')

print('Creating resource...')
resId = aws_api.api_controller.create_resource(idApi, 'myphiresource')

#deberia crear el zip la funcion de lambda?
print('Creating zip file to upload lambda function...')
#zipFile = aws_lambda.zip_my_file.create_zip_file(os.path.abspath('../aws_lambda/get_container_func.py'))
#zipFile = '/Users/marionevado/PycharmProjects/phiAws/aws_lambda/get_container_func.zip'

#print('uploading lambda function with zip file: ' +  zipFile + ' ...')
lambdaFuncArn = aws_lambda.lambda_ex.create_lambda_function('/Users/marionevado/PycharmProjects/phiAws/aws_lambda/get_container_func.zip', 'probandoFun',
                       'arn:aws:iam::471454180135:role/lambda_dynamo', 'get_container_func.lambda_handler')

#arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:471454180135:function:getContainer/invocations
pprint.pprint(lambdaFuncArn)
method_uri_root = 'arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/'
method_uri = method_uri_root + lambdaFuncArn + '/invocations'

print('Puting method and integration lambda function to resource...')
aws_api.api_controller.put_method(idApi, resId, 'GET')
aws_api.api_controller.put_method_integration(idApi, resId, 'GET', method_uri)