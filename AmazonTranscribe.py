
import boto3
import time
from S3 import S3

class AmazonTranscribe():
    def __init__(self, job_name, s3_uri):
        self.__connect()
        self.job_name = job_name
        self.s3_uri = s3_uri

    def __connect(self):
        self.transcribe_client = boto3.client('transcribe')

    def transcribe(self):
        print(self.s3_uri)
        self.transcribe_client.start_transcription_job(
            TranscriptionJobName=self.job_name,
            Media={'MediaFileUri': self.s3_uri},
            MediaFormat='wav',
            LanguageCode='pt-BR'
        )

        while True:
            status = self.transcribe_client.get_transcription_job(TranscriptionJobName=self.job_name)
            if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                break
            print("Not ready yet...")
            time.sleep(5)
            print(status)
