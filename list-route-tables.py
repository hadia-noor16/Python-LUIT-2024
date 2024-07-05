import boto3
ec2=boto3.client('ec2')

response = ec2.describe_route_tables()

for route in response["RouteTables"]:

    #print(route['RouteTableId'],route['VpcId'])

    for association in route['Associations']:  #since Associations is a key under RouteTables dict
        print(association["RouteTableAssociationId"])
        if 'SubnetId' in association:
            print(association['SubnetId'])

    for cidr in route['Routes']:   
        print(cidr['DestinationCidrBlock'])


#describe internet gatways

response2 = ec2.describe_internet_gateways()
#print(response2)

for res in response2['InternetGateways']:
    #print(res["InternetGatewayId"])
    for igid in res["Attachments"]:
        print(igid['VpcId'])
        for igw in res['Tags']:
            if 'Name' == igw['Key']:
                print(igw['Value'])

    

            
        