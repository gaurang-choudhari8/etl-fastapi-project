import boto3
from fastapi import UploadFile
class s3_service_class:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        #self.__access_key = access_key
        #self.__secret_key = secret_key
        self.s3_client=boto3.client('s3')

    def upload_file(self, file: UploadFile, name: str):
        pass
        

    def get_buckets(self, bucket_name: str):
        response = self.s3_client.list_buckets()

        bucketDict = response['Buckets']
        for bucket in bucketDict:

