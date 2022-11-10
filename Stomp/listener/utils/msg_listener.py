from stomp import ConnectionListener

from .filter import luminosity_level

class MsgListener(ConnectionListener):
    def on_error(self, message):
        print('received an error %s' % message.body)

    def on_message(self, frame):
        msg = luminosity_level(frame)
        if msg:
            print(msg)