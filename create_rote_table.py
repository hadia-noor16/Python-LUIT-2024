import boto3

ec2=boto3.client('ec2')

#response = ec2.create_route_table(
    #VpcId='vpc-0189588e72b5f397a'
#)

#print(response['RouteTable']['RouteTableId'])


#associte subnet with route table

associate = ec2.associate_route_table(
    RouteTableId='rtb-0d874b37889e61024',
    SubnetId='subnet-0883f9df603959725'
)

print(associate['AssociationId'])