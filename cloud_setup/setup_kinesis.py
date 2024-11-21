import boto3

def setup_kinesis_stream():
    kinesis_client = boto3.client('kinesis', region_name='ap-south-1')
    
    # Create Kinesis Stream
    response = kinesis_client.create_stream(
        StreamName='TrafficDataStream',
        ShardCount=1
    )
    print(f"Kinesis Stream created: {response['StreamDescription']['StreamName']}")

setup_kinesis_stream()
