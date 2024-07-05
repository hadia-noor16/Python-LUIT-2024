import boto3

ec2=boto3.client('ec2')

response = ec2.create_vpc(
    CidrBlock='11.0.0.0/16')


for vpc in response:
    print(vpc['Vpc'], vpc['VpcId'])
