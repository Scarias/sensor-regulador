from stomp import Connection, ConnectionListener

from utils.filter import out_range


N_SENSORS = 10


class MsgListener(ConnectionListener):
    data = dict()
    queue_empty = True

    def __init__(self, total_sensors):
        for i in range(total_sensors):
            self.data[i] = list()

    def on_error(self, frame):
        print('Error recibido: %s' % frame.body)

    def on_message(self, frame):
        # out-of-range data
        if out_range(frame):
            print('%s: Valor anormal en sensor %s' % tuple(frame.body.split(',')))
            return

        # local queueing for data
        value, sensor = map(tuple(frame.body.split(',')), int)
        if sensor not in self.data:
            print('Sensor desconocido: %s' % (sensor, value))
            return
        self.data[sensor].append(value)

        print('%s: Valor recibido desde sensor %s', (value, sensor))


conn = Connection([('localhost', 61613)])
conn.set_listener('sensor_listener', MsgListener(N_SENSORS))
conn.connect()
conn.subscribe(destination='/queue/sensors', id='1', ack='auto', transformation='jms-json')