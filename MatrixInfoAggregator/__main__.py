from os import _exit as os_exit
from sys import exit as sys_exit
from time import sleep

from connection.listener import MsgListener
from connection.sender import MsgSender

from utils.joiner import prepare_data


N_SENSORS = 10
SLEEP_TIME = 1


if __name__ == '__main__':

    try:
        main_listener = MsgListener(N_SENSORS)
        main_sender = MsgSender()

        while 1:
            # Get from sensors
            main_listener.get_message()

            # Check if have data
            if any(main_listener.data.values()):
                prepared_data = prepare_data(main_listener.data)

                # and send that data
                main_sender.send_message(exchange='', routing_key='expert', body=prepared_data)

            # Stop for a while
            sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print(' [-] Conexión terminada por el usuario.')
        try:
            sys_exit(0)
        except SystemExit:
            os_exit(0)

        """
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
        """