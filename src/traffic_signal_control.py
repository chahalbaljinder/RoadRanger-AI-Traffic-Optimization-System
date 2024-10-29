import boto3
import json

iot_client = boto3.client('iot-data')

def control_traffic_signal(signal_id, green_time, red_time):
    payload = {
        'signal_id': signal_id,
        'green_time': green_time,
        'red_time': red_time
    }
    response = iot_client.publish(
        topic=f"traffic/signals/{signal_id}",
        qos=1,
        payload=json.dumps(payload)
    )
    return response
