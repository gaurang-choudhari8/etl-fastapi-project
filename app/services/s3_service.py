import boto3
from fastapi import UploadFile
from botocore.exceptions import ClientError
from boto3.exceptions import S3UploadFailedError
class s3_service_class:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        #self.__access_key = access_key
        #self.__secret_key = secret_key
        self.s3_client=boto3.client('s3')

    def upload_file(self, file: UploadFile, key: str, bucket_name: str):
        try:
            with file.file as data:
                self.s3_client.upload_fileobj(data, bucket_name,key)
            return {
                "status": "Success",
                "description": "The file upload succeeded"
            }
        except ClientError as ce:
            return {
                "error": "The bucket does not exist",
                "description": str(ce)
            }
        except S3UploadFailedError as ufe:
            return {
                "error": "The upload failed",
                "description": str(ufe)
            }
        except Exception as ue:
            return {
                "error": "Unknown exception",
                "description": str(ue)
            }
        

    def get_buckets(self, bucket_name: str):
        response = self.s3_client.list_buckets()

        bucketDict = response['Buckets']
        for bucket in bucketDict:
            pass
