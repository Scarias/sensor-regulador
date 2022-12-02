from time import sleep

from connection.listener import MsgListener, listener
from connection.sender import sender

from utils.joiner import prepare_data


N_SENSORS = 10
SLEEP_TIME = 1


if __name__ == '__main__':

    main_listener = MsgListener(N_SENSORS)

    listener_conn = listener(main_listener)
    sender_conn = sender()

    while 1:
        print(main_listener.data)
        if any(main_listener.data.values()):
            prepared_data = prepare_data(main_listener.data)
            sender_conn.send(
                body=prepared_data,
                destination='/queue/expert',
                content_type='text/plain'
            )
            print("Sended data:", prepared_data)

        sleep(SLEEP_TIME)