import boto3

def filtering_object_extension(client,bucket,extension):
    keys=[]
    response=s3.list_objects_v2(Bucket=bucket)

    for content in response["Contents"]:
        if (extension in content["Key"][-(len(extension)):]):
            keys.append(content["Key"])
    return keys


def filtering_all_object(client,bucket,prefix=""):
    keys=[]
    response=s3.list_objects_v2(Bucket=bucket,Prefix=prefix)

    for content in response["Contents"]:
        keys.append(content["Key"])
    return keys


s3=boto3.client('s3')

if __name__ == "__main__":

    keys=filtering_object_extension(s3,'hadia-doing-boto3demo',".txt")
    print(keys)
    keys=filtering_all_object(s3,'hadia-doing-boto3demo')
    print(keys)