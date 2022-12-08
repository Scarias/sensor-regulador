import ssl
import pika


class AWSPikaClient:
    conn = None
    channel = None

    def __init__(self, broker_id=None, user=None, password=None, region=None, aws=False) -> None:
        if aws:
            # SSL Context
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

            url = f'amqps://{user}:{password}@{broker_id}.mq.{region}.amazonaws.com:5671'
            parameters = pika.URLParameters(url)
            parameters.ssl_options = pika.SSLOptions(context=ssl_context)

            self.conn = pika.BlockingConnection(parameters)
            self.channel = self.conn.channel()
        else:
            parameters = pika.ConnectionParameters('localhost')
            self.conn = pika.BlockingConnection(parameters)
            self.channel = self.conn.channel()
