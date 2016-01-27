import zip_my_file
import lambda_client
import pprint

zip_my_file.create_zip_file('get_container_func.py')

# delte function if exists
#delete zip file necesario?

with open('get_container_func.zip', 'rb') as fp:
    zipdata = fp.read()
    response = lambda_client.create_function('creandofun', 'arn:aws:iam::471454180135:role/lambda_dynamo', 'get_container_func.lambda_handler', zipdata)

#role expression
#arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+
# ex arn:aws:iam::471454180135:role/lambda_dynamo

#pprint.pprint(response)