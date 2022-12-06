from utils.filter import out_range
from utils.base_client import AWSPikaClient


class MsgListener(AWSPikaClient):
    data = dict()

    def __init__(self, total_sensors):
        super().__init__()
        for i in range(1, total_sensors+1):
            self.data[i] = list()

    def on_error(self, body):
        if body:
            print('Error recibido: %s' % body)

    def on_message(self, ch, method, properties, body):
        # out-of-range data
        if out_range(body):
            print('%s: Valor anormal en sensor %s' % tuple(body.body.split(',')))
            return

        # local queueing for data
        value, sensor = tuple(body.body.split(','))
        value = float(value)
        sensor = int(sensor)
        if sensor not in self.data:
            print('Sensor desconocido: %s' % (sensor, ))
            return
        self.data[sensor].append(value)

        print('%s: Valor recibido desde sensor %s' % (value, sensor))

    def listen_messages(self, queue='sensors'):
        self.channel.basic_consume(queue=queue, on_message_callback=self.on_message, auto_ack=True)

        print(' [*] Escuchando sensores...')
        self.channel.start_consuming()

    def get_message(self, queue='sensors'):
        self.channel.queue_declare(queue)
        method, header, body = self.channel.basic_get(queue=queue)
        if method:
            self.channel.basic_ack(method.delivery_tag)
            self.on_message(queue, method, header, body)
        else:
            self.on_error(body)

    def close(self):
        self.channel.close()
        self.conn.close()
