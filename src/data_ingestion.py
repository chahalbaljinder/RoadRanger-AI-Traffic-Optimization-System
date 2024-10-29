import boto3
import json

iot_client = boto3.client('iot-data')
kinesis_client = boto3.client('kinesis')

def ingest_iot_data(device_id, sensor_data):
    topic = f"traffic/sensors/{device_id}"
    response = iot_client.publish(
        topic=topic,
        qos=1,
        payload=json.dumps(sensor_data)
    )
    return response

def ingest_gps_data(stream_name, gps_data):
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(gps_data),
        PartitionKey="partitionKey"
    )
    return response
