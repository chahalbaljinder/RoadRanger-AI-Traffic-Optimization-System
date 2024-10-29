import boto3

kinesis_client = boto3.client('kinesis')

def create_kinesis_stream(stream_name, shard_count=1):
    response = kinesis_client.create_stream(
        StreamName=stream_name,
        ShardCount=shard_count
    )
    return response