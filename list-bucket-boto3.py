import boto3

s3=boto3.client('s3')

response= s3.list_buckets()

#print(response)

buckets=response['Buckets']
print(type(buckets))

for bucket in buckets:
    print(bucket['Name'])



#print(buckets)