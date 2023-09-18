import json
import boto3
from time import gmtime, strftime
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tempconv')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
def lambda_handler(event, context):
    F = int(event['celsius']) * 9 / 5 + 32;
    K = int(event['celsius']) + 273.15;
    response = table.put_item(
        Item={
            'Fvalue': str(F),
	          'Kvalue': str(K),
            'LatestGreetingTime':now
            })
    return {
    'statusCode': 200,
    'body': json.dumps('Farhenheit :' + str(F) + 'Kelvin:' + str(K))
    }
