import boto3

# Initialize an S3 client
s3 = boto3.client('s3')

def create_presigned_url(bucket_name: str, object_name: str, expiration: int = 3600) -> str:
    """
    Generate a presigned URL for downloading an object from an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        object_name (str): The key (name) of the object within the bucket.
        expiration (int, optional): The expiration time in seconds for the presigned URL (default is 3600 seconds).

    Returns:
        str: The presigned URL that allows downloading the specified object.
    """
    response = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_name},
        ExpiresIn=expiration
    )
    
    return response

# Create a presigned URL for 'test2.txt' in 'hadia-doing-boto3demo' bucket with default expiration
url = create_presigned_url('hadia-doing-boto3demo', 'test2.txt')

# Print the generated presigned URL
print(url)
