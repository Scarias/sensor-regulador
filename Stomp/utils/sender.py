from base_client import AWSPikaClient

class SenderLocalNoAmq(AWSPikaClient):
    def __init__(self):
        super().__init__(aws=False)

    def send(self, queue_name, message):
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(" [x] Sent %r" % message)
    

