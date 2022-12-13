from time import sleep
from dotenv import dotenv_values

from utils.msg_listener import get_sqs, get_message


config = dotenv_values('.env')

SLEEP_TIME = 1
SQS_URL = config['SQS_URL']


if __name__ == '__main__':
    sqs = get_sqs()

    while 1:
        msg = get_message(sqs, SQS_URL)
        print(f' [x] Recibido: {msg}')
