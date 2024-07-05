import boto3

ec2=boto3.client('ec2')

#response = ec2.create_internet_gateway(
#)

#print(response)

#attach igw to VPC

attach = ec2.attach_internet_gateway(
    InternetGatewayId='igw-04b613ed58d1409ca',
    VpcId='vpc-0189588e72b5f397a'
)

print(attach)