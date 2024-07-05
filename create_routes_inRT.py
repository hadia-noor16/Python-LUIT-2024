import boto3

ec2=boto3.client('ec2')

igw_id='igw-04b613ed58d1409ca'
des_cidr='0.0.0.0/0'
rt_id='rtb-0d874b37889e61024'

response = ec2.create_route(
    DestinationCidrBlock=des_cidr,
    GatewayId=igw_id,
    RouteTableId=rt_id
)

print(response)

