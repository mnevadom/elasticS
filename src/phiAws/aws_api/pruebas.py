import api_client
import pprint
import boto3

client = boto3.client('apigateway')

#pprint.pprint(api_client.get_method('wrie62gtmd', 'v35hj3', 'GET'))

uriLambdaFunc = 'arn:aws:apigateway:us-east-1:aws_lambda:path/2015-03-31/functions/arn:aws:aws_lambda:us-east-1:471454180135:function:getContainer/invocations'
#pprint.pprint(api_client.put_integration_method('wrie62gtmd', '5s1ftd', 'POST', uriLambdaFunc))


#pprint.pprint(api_client.create_resource('wrie62gtmd', 'v35hj3', 'pruebares'))

#resMethod = api_client.put_resource_method('wrie62gtmd', 'v35hj3', 'GET', '')

pprint.pprint(api_client.get_resources('wrie62gtmd', 3))

#resIntegr = api_client.put_integration_method('wrie62gtmd', 'v35hj3', 'GET', uriLambdaFunc)
