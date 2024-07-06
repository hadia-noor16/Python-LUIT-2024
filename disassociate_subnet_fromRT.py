#disassociate route table from subnet
#to get association Id, we need to run "describe_route_table" for this RT, as associateion id is not visible in UI


import boto3

ec2=boto3.client('ec2')

response = ec2.describe_route_tables(
    RouteTableIds=[
        'rtb-0d874b37889e61024'
    ]
)

print(response)


for association in response['RouteTables']:  #RouteTables is a key in response, RoutTable is a list of dictionaries
    for associate in association['Associations']:  #Associations is a key, with another list of Dictioneries
        print(associate['RouteTableAssociationId'])  #RouteTableAssociationId is another key within
# now we have got association id, use it in below command

disassociate = ec2.disassociate_route_table(    
    AssociationId='rtbassoc-08fb9d6b29248041c'
)                                                  
print(disassociate)