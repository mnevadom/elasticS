import zip_my_file
import lambda_client
import pprint


# delte function if exists
#delete zip file necesario?

def create_lambda_function(path, name, role, handler):
    #zip_my_file.create_zip_file('get_container_func.py')
    response = lambda_client.get_function(name)
    if (response is None):
        with open(path, 'rb') as fp:
            zipdata = fp.read()
            response = lambda_client.create_function(name, role, handler, zipdata)
            return response['FunctionArn']
    else:
        print('Lambda function ' + name + ' already exists')
        config = response['Configuration']
        return config['FunctionArn']

#role expression
#arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+
# ex arn:aws:iam::471454180135:role/lambda_dynamo
#pprint.pprint(response)

#TESTING

#create_lambda_function('/Users/marionevado/PycharmProjects/phiAws/aws_lambda/get_container_func.zip', 'probandoFun',
 #                      'arn:aws:iam::471454180135:role/lambda_dynamo', 'get_container_func.lambda_handler')