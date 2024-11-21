import boto3

def setup_iot_core():
    iot_client = boto3.client('iot', region_name='ap-south-1')
    
    # Create IoT Thing (Device)
    response = iot_client.create_thing(
        thingName='SmartTrafficSensor',
        thingTypeName='SensorType',
        attributePayload={'attributes': {'type': 'sensor'}}
    )
    print(f"Created IoT Thing: {response['thingName']}")

setup_iot_core()
