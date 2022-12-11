import numpy as np
import time

import logging

from utils.msg_sender import SenderLocalNoAmq


class Messenger:
    def __init__(self):
        self.sender = SenderLocalNoAmq()

    def send(self, queue_name, message):
        self.sender.send(queue_name, message)

def process():
    messenger = Messenger()
    while True:
        t = time.localtime()
        current_time = time.strftime("%d/%m/%Y %H:%M:%S", t)
        msj = str(np.random.random() * 5 + np.random.randn()) + ",2"
        logging.info(msj + " " + current_time)
        messenger.send('sensors', msj)
        time.sleep(2)
