import api_client
import pprint
import boto3


nameApi = 'PhiSc'
rest_api = api_client.create_rest_api(nameApi, 'phi api to manage containers', '')
idApi = rest_api['id']

print('create api %s, with ID %s', nameApi, idApi)

# si da error algo por aqui que borre el api y vuelva a crear en la sig, que sino se pierde el id
# sino con el get apis puedo con el nombre sacar su id

#print('rest api created with name %s and id %s', )
#print(id)
#api id wrie62gtmd    / res id v35hj3    /    parent res id   w2ynbeich8

resources = api_client.get_resources(idApi, 1)
resourcesList = resources['items']
parentResource = resourcesList[0]
parentResId = parentResource['id']

print('Parent resource / with id %d ', parentResId)

#pprint.pprint(api_client.get_rest_api('uv20wv3ee9'))
resName = 'createcont'
newRes = api_client.create_resource(idApi, parentResId, resName)

print('create resource: ')
pprint.pprint(newRes)
resId = newRes['id']


# put integration, wit GET or PUT
# need to get the uri of aws_lambda function, for now: arn:aws:apigateway:us-east-1:aws_lambda:path/2015-03-31/functions/arn:aws:aws_lambda:us-east-1:471454180135:function:getContainer/invocations
uriLambdaFunc = 'arn:aws:apigateway:us-east-1:aws_lambda:path/2015-03-31/functions/arn:aws:aws_lambda:us-east-1:471454180135:function:getContainer/invocations'

# first we create the method
resMethod = api_client.put_resource_method(idApi, resId, 'GET', '')

# then we put an integration on it
resIntegr = api_client.put_integration_method(idApi, resId, 'GET', uriLambdaFunc)
