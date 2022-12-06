import ssl
import pika


class AWSPikaClient:
    conn = None
    channel = None

    def __init__(self, rabbitmq_url=None) -> None:
        if rabbitmq_url:
            # SSL Context
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

            parameters = pika.URLParameters(rabbitmq_url)
            parameters.ssl_options = pika.SSLOptions(context=ssl_context)

            self.conn = pika.BlockingConnection(parameters)
            self.channel = self.conn.channel()
        else:
            parameters = pika.ConnectionParameters('localhost')
            self.conn = pika.BlockingConnection(parameters)
            self.channel = self.conn.channel()
