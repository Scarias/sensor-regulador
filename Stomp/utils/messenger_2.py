from sender import SenderLocalNoAmq
import numpy as np
import time

class Messenger:
    def __init__(self):
        self.sender = SenderLocalNoAmq()

    def send(self, queue_name, message):
        self.sender.send(queue_name, message)

if __name__ == '__main__':
    messenger = Messenger()
    while True:
        messenger.send('sensors', str(np.random.random() * 5 + np.random.randn()) + ",2")
        time.sleep(2)