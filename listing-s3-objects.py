import boto3

# Initialize an S3 client
s3 = boto3.client('s3')

def upload_and_list_objects(filename: str, bucket_name: str) -> None:
    """
    Uploads a file to an S3 bucket and then lists all objects in the bucket.

    Args:
        filename (str): The name of the file to upload.
        bucket_name (str): The name of the S3 bucket.

    Returns:
        None
    """
    # Upload the specified file to the specified S3 bucket
    s3.upload_file(filename, bucket_name, filename)

    # List objects in the specified S3 bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Print the type of 'response' (dict)
    print(type(response))

    # Print the entire response object
    print(response)

    # Iterate through each object in the bucket and print its key (filename)
    for content in response['Contents']:
        print(content['Key'])

# Call the function to upload a file and list objects in the bucket
upload_and_list_objects('newest.txt', 'hadia-doing-boto3demo')
