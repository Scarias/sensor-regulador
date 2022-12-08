from utils.msg_listener import ListenerLocalNoAmq

if __name__ == '__main__':
    client = ListenerLocalNoAmq()
    client.listen('sensors')
