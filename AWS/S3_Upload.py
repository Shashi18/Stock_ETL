import config
import boto3

class AWS_S3():
    def __init__(self, bucket, access_key=None, secret_key=None):
        self.bucket = bucket
        self.client = boto3.client('s3', aws_access_key_id=config.access_key, aws_secret_access_key=config.secret_key)
        self.region_name = boto3.session.Session()

    def list_all_buckets(self):
        return self.client.list_buckets()['Buckets']
        
    def upload_to_bucket(self, file, object_name=None):
        try:
            self.client.upload_file(file, self.bucket, object_name)
        except ClientError as e:
            raise ValueError(e)
        
    def download_from_bucket(self, file):
        temp = ''
        self.client.download_file(self.bucket, file, temp)
        return temp
