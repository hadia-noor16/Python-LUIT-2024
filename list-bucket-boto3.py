import boto3

# Initialize an S3 client
s3 = boto3.client('s3')

def list_s3_buckets():
    """
    Fetches and prints the names of all S3 buckets in the AWS account.

    Returns:
        None
    """
    # Fetch the response containing information about all S3 buckets
    response = s3.list_buckets()

    # Extract the list of buckets from the response
    buckets = response['Buckets']
    
    # Print the type of 'buckets' (list)
    print(type(buckets))

    # Iterate through each bucket and print its name
    for bucket in buckets:
        print(bucket['Name'])

# Uncomment the following line to print the raw response object
# print(response)

# Uncomment the following line to print the list of bucket names
# print(buckets)

# Call the function to list and print bucket names
list_s3_buckets()
