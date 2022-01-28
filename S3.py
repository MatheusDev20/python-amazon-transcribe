
import boto3

class S3:
    def __init__(self):
        self.__connect()
        self.bucket_name = 'my-app-gobarberr'
        self.bucket_region = 'us-east-1'

    def __connect(self):
        self.s3_client = boto3.resource(
            's3',
            aws_access_key_id='',
            aws_secret_access_key=''
        )

    def generateS3FileLink(self, path_file):
        return f'https://{self.bucket_name}.s3.{self.bucket_region}.amazonaws.com/{path_file}'

    def upload(self, s3_file, content):
        try:
            ret = self.s3_client.Object(
                self.bucket_name,
                s3_file).put(
                    Body=content,
                    ACL='public-read'
                )
            
            link = self.generateS3FileLink(s3_file)
            return link

        except Exception as e:
            print('An error ocurred')


