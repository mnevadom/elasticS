import boto3
import pprint

client = boto3.client('lambda')
pp = pprint.PrettyPrinter(indent=4)

def get_functions():
    return client.list_functions()

def get_function(name):
    return client.get_function(
        FunctionName='getContainer'
    )

