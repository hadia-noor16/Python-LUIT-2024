import boto3

# Initialize an S3 client
s3 = boto3.client('s3')

# Create a new S3 bucket with the specified name 'hadia-doing-boto3demo'
response = s3.create_bucket(
    Bucket='hadia-doing-boto3demo'
)

# Print the creation date of the bucket
print(response['ResponseMetadata']['HTTPHeaders']['date'])