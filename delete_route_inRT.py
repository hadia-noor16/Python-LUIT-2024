import boto3

ec2=boto3.client('ec2')

#response = ec2.delete_route(
    #DestinationCidrBlock='0.0.0.0/0',
    #RouteTableId='rtb-0d874b37889e61024',
#)

#print(response)

#detach internet gateway

#detach = ec2.detach_internet_gateway(
   # InternetGatewayId='igw-04b613ed58d1409ca',
   # VpcId='vpc-0189588e72b5f397a'
#)

#print(detach)

#delete internet gateway

delete = ec2.delete_internet_gateway(
    InternetGatewayId='igw-04b613ed58d1409ca'
)

print(delete)