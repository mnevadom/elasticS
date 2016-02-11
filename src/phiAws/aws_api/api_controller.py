import api_client
import pprint
import boto3


def create_api(nameApi):
    rest_api = api_client.create_rest_api(nameApi, 'phi api to manage containers', '')
    idApi = rest_api['id']
    print('create api %s, with ID %s', nameApi, idApi)
    return idApi


# si da error algo por aqui que borre el api y vuelva a crear en la sig, que sino se pierde el id
# sino con el get apis puedo con el nombre sacar su id

# print('rest api created with name %s and id %s', )
# print(id)
# api id wrie62gtmd    / res id v35hj3    /    parent res id   w2ynbeich8

# el parent id sacarlo mejor viendo cual tiene el path a /
def create_resource(idApi, resName):
    resources = api_client.get_resources(idApi, 1)
    resourcesList = resources['items']
    parentResource = resourcesList[0]
    parentResId = parentResource['id']
    print('Parent resource / with id %d ', parentResId)
    # pprint.pprint(api_client.get_rest_api('uv20wv3ee9'))
    newRes = api_client.create_resource(idApi, parentResId, resName)
    print('create resource: ')
    # pprint.pprint(newRes)
    resId = newRes['id']
    print('res id : ' + resId)
    return resId


# put integration, wit GET or PUT
def put_method(idApi, resId, methodType):
    resMethod = api_client.put_resource_method(idApi, resId, methodType, '')


def put_method_integration(idApi, resId, methodType, uriLambdaFunc):
    resIntegr = api_client.put_integration_method(idApi, resId, methodType, uriLambdaFunc)


def delete_rest_api(name):
    apis = api_client.get_rest_apis()
    for api in apis['items']:
        if (api['name'] == name):
            api_client.delete_rest_api(api['id'])