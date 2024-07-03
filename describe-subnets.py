import boto3

ec2=boto3.client('ec2')

response = ec2.describe_subnets()

for subnet in response['Subnets']:
    #print(subnet['CidrBlock'],subnet['VpcId'],subnet['SubnetId'])
    if 'Tags' in subnet:
        for tag in subnet['Tags']:
            if 'Name' == tag['Key']:
        
                print(subnet['SubnetId'],subnet['CidrBlock'],subnet['VpcId'],tag['Value'])
