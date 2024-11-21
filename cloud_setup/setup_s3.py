import boto3

def setup_s3_bucket():
    s3_client = boto3.client('s3', region_name='ap-south-1')
    
    # Create S3 Bucket for storing traffic data
    s3_client.create_bucket(
        Bucket='smart-traffic-data',
        CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
    )
    print("S3 Bucket 'smart-traffic-data' created.")

setup_s3_bucket()
