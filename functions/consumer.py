import base64

def handler(event, context):
    records = event['Records']

    for record in records:
        data = record['kinesis']['data']
        decoded_data = base64.b64decode(data).decode('utf-8')
        # parsed_data = json.loads(decoded_data)
        print(decoded_data)

    return {
        'statusCode': 200,
        'body': 'Success',
    }