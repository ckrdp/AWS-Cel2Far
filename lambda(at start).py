import json
def lambda_handler(event, context):
    F = int(event['celsius']) * 9 / 5 + 32;
    K = int(event['celsius']) + 273.15;
    return {
    'statusCode': 200,
    'body': json.dumps('Farhenheit :' + str(F) + 'Kelvin:' + str(K))
    }