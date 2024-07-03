import boto3

ec2=boto3.client('ec2')

response = ec2.describe_vpcs()

#print(response['Vpcs'])

for vpc in response['Vpcs']:
    print(vpc['VpcId'], vpc['CidrBlock'], vpc ['IsDefault'])   #grabbing simple values

#for res in response['Vpcs']:
   # for cidr in res['CidrBlockAssociationSet']:        #grabbing value for Cidrblock that's under dict CideBlockAssociationSet
       # print (cidr['CidrBlock'])


for vpc in response['Vpcs']:
    if 'Tags' in vpc:#checkigifthekey'Tags'exists
        #print (vpc['Tags'])
        for tag in vpc['Tags']:       
            if 'Name' == tag['Key']:
                print(tag['Key'],tag['Value'])


        
      
            
                          


