import stomp
import numpy as np
import time


def process():
    np.random.seed(0)

    conn = stomp.Connection([('localhost', 61613)])
    conn.connect()

    while True:
        conn.send(
            body=str(np.random.random() * 5 + np.random.randn()) + ",1",
            destination="/queue/sensors",
            content_type="text/plain",
            receipt="123"
        )
        time.sleep(2)
