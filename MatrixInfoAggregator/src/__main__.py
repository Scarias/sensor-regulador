from time import sleep

from .connection.listener import conn as sensor_conn
from .connection.sender import conn as expert_conn
from .utils.joiner import prepare_data


SLEEP_TIME = 1 # in seconds


if __name__ == '__main__':
    while 1:
        data = sensor_conn.get_listener('sensor_listener').data

        if any(data.values()):
            expert_conn.send(
                body=prepare_data(data),
                destination='/queue/expert',
                content_type='text/plain'
            )

        sleep(SLEEP_TIME)