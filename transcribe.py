from upload_file_s3 import UploadFile
from AmazonTranscribe import AmazonTranscribe
from upload_file_s3 import UploadFile

class Transcribe(AmazonTranscribe):
    def __init__(self, audio, job_name):
        self.local_path = audio
        self.job_name = job_name
        self.transcribe_client = self.__prepareTranscribe()

    def __prepareTranscribe(self):
        return AmazonTranscribe(self.job_name, self.local_path)

    def stt(self):
        s3_file_link = UploadFile().sendToS3(self.local_path)
        transcribe_service = AmazonTranscribe(self.job_name, s3_file_link)
        transcribe_service.transcribe()
        

