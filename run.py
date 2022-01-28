
from transcribe import Transcribe
from random import random
path = 'audios/carioca_puto.wav'
job_name = 'teste' + str(random())
stt_client = Transcribe(path, job_name)

def run():
    stt_client.stt()

if __name__ == '__main__':
    run()