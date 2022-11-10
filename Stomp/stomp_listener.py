import stomp
import time
from stomp import ConnectionListener


class MsgListener(ConnectionListener):
    def on_error(self, message):
        print('received an error "%s"' % message.body)

    def on_message(self, frame):
        print('received a message "%s"' % frame.body)


conn = stomp.Connection([('127.0.0.1', 61613)])
conn.set_listener('stomp_listener', MsgListener())
conn.connect()
conn.subscribe(destination="/queue/test", id=1, ack='auto', transformation="jms-json")

while 1:
    time.sleep(2)