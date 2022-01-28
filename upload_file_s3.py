from S3 import S3
import os


class UploadFile(S3):
    def __init__(self):
        S3.__init__(self)


    def sendToS3(self, local_path):
        with open(local_path, 'rb') as f:
            content = f.read()
            file_s3_link = self.upload('teste_transcript.wav', content)

        return file_s3_link
