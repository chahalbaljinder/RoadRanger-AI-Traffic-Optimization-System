import boto3

lambda_client = boto3.client('lambda')

def create_lambda_function(function_name, role_arn, handler, zip_file):
    with open(zip_file, 'rb') as f:
        zipped_code = f.read()

    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime='python3.8',
        Role=role_arn,
        Handler=handler,
        Code={'ZipFile': zipped_code},
        Timeout=300,  # Set the timeout to 5 minutes
        MemorySize=128  # Memory allocated to the function
    )
    return response