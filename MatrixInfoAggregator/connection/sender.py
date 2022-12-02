from stomp import Connection


def sender():
    conn = Connection([('b-770ca97b-c743-4527-9daf-e275398a5239.mq.sa-east-1.amazonaws.com', 5671)])
    conn.connect()

    return conn