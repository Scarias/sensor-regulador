from base_client import AWSPikaClient

class ListenerLocalNoAmq(AWSPikaClient):
    def __init__(self):
        super().__init__(aws=False)

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
    
    def listen(self, queue_name):
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
    

if __name__ == '__main__':
    client = ListenerLocalNoAmq()
    client.listen('sensors')
    