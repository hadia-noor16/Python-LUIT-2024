import boto3

ec2=boto3.client('ec2')

cidr_block='10.0.3.0/24'
vpc_id='vpc-0189588e72b5f397a'

def create_subnet(client,cidr_block,vpc_id):

    response = ec2.create_subnet(CidrBlock=cidr_block,VpcId=vpc_id)
    return response



vpc=create_subnet(ec2,cidr_block,vpc_id)

print(vpc['Subnet']['SubnetId'])