import stomp
import numpy as np
import time

def process():
    np.random.seed(1)

    conn = stomp.Connection([('localhost', 61613)])
    conn.connect()

    while True:
        conn.send(
            body=str(np.random.random() * 5 + np.random.randn()) + ",2",
            destination="/queue/test",
            content_type="text/blah",
            receipt="123"
        )
        time.sleep(2)