import boto3
import json
import ast
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Predictions')

def lambda_handler(event, context):
    # TODO implement
    runtime_client = boto3.client('runtime.sagemaker')
    endpoint_name = 'xgboost-2024-07-02-08-22-07-295'
    
    sample = '{},{},{},{}'.format(ast.literal_eval(event['body'])['x1'],
                                  ast.literal_eval(event['body'])['x2'],
                                  ast.literal_eval(event['body'])['x3'],
                                  ast.literal_eval(event['body'])['x4'])
    
    response = runtime_client.invoke_endpoint(EndpointName = endpoint_name, ContentType = 'text/csv', Body = sample)
    
    result = int(float(response['Body'].read().decode('ascii')))
    
    timestamp = datetime.now().isoformat()
    table.put_item(Item={'timestamp': timestamp, 'prediction': result})
    
    
    return {
        'statusCode': 200,
        'body': json.dumps({'prediction' : result})
    }
