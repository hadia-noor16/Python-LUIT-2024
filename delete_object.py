import boto3
s3=boto3.client('s3')

bucket="hadia-doing-boto3demo"
key="newest.txt"


response = s3.delete_object(
    Bucket=bucket,
    Key=key)