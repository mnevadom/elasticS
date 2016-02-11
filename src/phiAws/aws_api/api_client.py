import boto3

client = boto3.client('apigateway')


def delete_rest_api(idApi):
    return client.delete_rest_api(
        restApiId=idApi
    )


def get_rest_apis():
    return client.get_rest_apis(
            limit=123
    )


def get_rest_api(name):
    return client.get_rest_api(
            restApiId=name
    )


def create_rest_api(name, description, cloneName):
    return client.create_rest_api(
            name=name,
            description=description,
            cloneFrom=cloneName
    )


def create_resource(apiId, parentResource, path):
    return client.create_resource(
            restApiId=apiId,
            parentId=parentResource,
            pathPart=path
    )


def get_resources(apiId, limit):
    return client.get_resources(
            restApiId=apiId,
            limit=limit
    )


def put_resource_method(restApiId, resourceId, httpMethod, authType):
    return client.put_method(
            restApiId=restApiId,
            resourceId=resourceId,
            httpMethod=httpMethod,
            authorizationType=authType
    )


def get_method(restApiId, resourceId, httpMethod):
    return client.get_method(
            restApiId=restApiId,
            resourceId=resourceId,
            httpMethod=httpMethod
    )


def get_integration_method(restApiId, resourceId, httpMethod):
    return client.get_integration(
            restApiId=restApiId,
            resourceId=resourceId,
            httpMethod=httpMethod
    )


def put_integration_method(restApiId, resourceId, httpMethod, uri):
    return client.put_integration(
            restApiId=restApiId,
            resourceId=resourceId,
            httpMethod=httpMethod,
            type='AWS',
            integrationHttpMethod=httpMethod,
            uri=uri
    )
