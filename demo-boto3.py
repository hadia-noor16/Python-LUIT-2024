import boto3
s3 = boto3.client('s3')

response = s3.create_bucket(

    Bucket='hadia-doing-boto3demo'
)
print(response['ResponseMetadata']['HTTPHeaders']['date'])