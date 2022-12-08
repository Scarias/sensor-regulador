from os import _exit as os_exit
from sys import exit as sys_exit
from dotenv import dotenv_values
from time import sleep

from connection.listener import MsgListener
from connection.sender import MsgSender
from utils.clean_data import clean_data

from utils.joiner import prepare_data


config = dotenv_values('.env')

N_SENSORS = 10
SLEEP_TIME = 1


if __name__ == '__main__':

    try:
        main_listener = MsgListener(N_SENSORS)
        main_sender = MsgSender(
            config['AWS_BROKER_ID'],
            config['AWS_USER'],
            config['AWS_PASSWORD'],
            config['AWS_REGION']
        )

        while 1:
            # Get from sensors
            main_listener.get_message()

            # Check if have data
            if any(main_listener.data.values()):
                prepared_data = prepare_data(main_listener.data)

                # and send that data
                main_sender.send_message(exchange='', routing_key='expert', body=prepared_data)

                # clean data to not send repeated messages
                clean_data(main_listener.data)

            # Stop for a while
            sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print(' [-] Conexión terminada por el usuario.')
        try:
            main_listener.close()
            main_sender.close()
            sys_exit(0)
        except SystemExit:
            os_exit(0)
