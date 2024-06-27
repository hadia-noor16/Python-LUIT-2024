import boto3

s3=boto3.client('s3')

res=s3.upload_file('newest.txt', 'hadia-doing-boto3demo', 'newest.txt')

response = s3.list_objects_v2(
    Bucket='hadia-doing-boto3demo')



print(type(response))

print(response)
for content in response['Contents']:
    print(content['Key'])
