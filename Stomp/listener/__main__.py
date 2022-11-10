import stomp
import time

from utils.msg_listener import MsgListener

if __name__ == '__main__':
    conn = stomp.Connection([('localhost', 61613)])
    conn.set_listener('stomp_listener', MsgListener())
    conn.connect()
    conn.subscribe(destination="/queue/test", id=1, ack='auto', transformation="jms-json")

    while 1:
        time.sleep(2)