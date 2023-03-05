import boto3
import json
import random
import time

kinesis = boto3.client('kinesis', region_name='us-east-1')
stream_name = 'stream-name-tes'

def generate_telemetry():
    while True:
        temperature = 20 + random.random() * 10
        wind = random.random() * 10
        pressure = 980 + random.random() * 40
        telemetry = {'temperature': temperature, 'wind': wind, 'pressure': pressure}
        params = {'Data': json.dumps(telemetry), 'PartitionKey': '1234', 'StreamName': stream_name}
        response = kinesis.put_record(**params)
        print(response)
        time.sleep(0.5)

generate_telemetry()