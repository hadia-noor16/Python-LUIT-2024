import boto3
import os
from filtering_extensions_boto3 import filtering_all_object    #importing list function from filtering_extensions_boto3.py

s3=boto3.client('s3')

if __name__ == "__main__":

    bucket='hadia-doing-boto3demo'
    key='test.txt'
    filename='test.txt'

    def download_objects(client,bucket,key,filename):

        client.download_file(bucket, key,filename)

    keys=filtering_all_object(s3,bucket)   #function called from filtering_extensions_boto3.py
    for key in keys:
        if '/' == key[-1]:  #checking if this is folder with last character as /
            try:
                os.mkdir(key)  
            except:
                pass
        else:
            download_objects(s3,bucket,key,key)