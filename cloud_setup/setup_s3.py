import boto3

s3 = boto3.client('s3')

def create_s3_bucket(bucket_name, region=None):
    create_bucket_config = {}
    if region:
        create_bucket_config = {'LocationConstraint': region}
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration=create_bucket_config
    )
    return response