from utils.base_client import AWSPikaClient


class MsgSender(AWSPikaClient):
    def __init__(self, broker_id, user, password, region) -> None:
        super().__init__(broker_id, user, password, region)

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

    def close(self):
        self.channel.close()
        self.conn.close()
