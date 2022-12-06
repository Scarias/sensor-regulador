from utils.base_client import AWSPikaClient


class MsgSender(AWSPikaClient):
    def __init__(self) -> None:
        super().__init__('amqps://b-8b498cb5-9d99-4ed2-acde-1e582a552c11.mq.sa-east-1.amazonaws.com:5671')

    def declare_queue(self, queue):
        print(f"Declarando queue {queue}")
        self.channel.queue_declare(queue)

    def send_message(self, exchange, routing_key, body):
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body
        )
        print(' [*] Datos enviados a Amazon MQ.')

"""
def sender():
    conn = Connection([('b-770ca97b-c743-4527-9daf-e275398a5239.mq.sa-east-1.amazonaws.com', 5671)])
    conn.connect()

    return conn
"""