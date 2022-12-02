from stomp import Connection, ConnectionListener

from utils.filter import out_range


class MsgListener(ConnectionListener):
    data = dict()
    queue_empty = True

    def __init__(self, total_sensors):
        for i in range(1, total_sensors+1):
            self.data[i] = list()

    def on_error(self, frame):
        print('Error recibido: %s' % frame.body)

    def on_message(self, frame):
        # out-of-range data
        if out_range(frame):
            print('%s: Valor anormal en sensor %s' % tuple(frame.body.split(',')))
            return

        # local queueing for data
        value, sensor = tuple(frame.body.split(','))
        value = float(value)
        sensor = int(sensor)
        if sensor not in self.data:
            print('Sensor desconocido: %s' % (sensor, ))
            return
        self.data[sensor].append(value)

        print('%s: Valor recibido desde sensor %s' % (value, sensor))


def listener(msg_list: MsgListener):
    conn = Connection([('localhost', 61613)])
    conn.set_listener('sensor_listener', msg_list)
    conn.connect()
    conn.subscribe(destination='/queue/sensors', id='1', ack='auto', transformation='jms-json')

    return conn