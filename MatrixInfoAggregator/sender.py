from stomp import Connection
from time import sleep

from listener import data
from utils.joiner import prepare_data


if __name__ == "__main__":
    conn = Connection([('b-770ca97b-c743-4527-9daf-e275398a5239.mq.sa-east-1.amazonaws.com', 5671)])
    conn.connect()

    while 1:
        print(data)
        if any(data.values()):
            conn.send(
                body=prepare_data(data),
                destination='/queue/expert',
                content_type='text/plain'
            )
            print("Sended data:", prepare_data(data))

        sleep(1)