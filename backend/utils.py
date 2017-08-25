import traceback

import pika
from pika.exceptions import ConnectionClosed


def reconnect(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
            except ConnectionClosed:
                traceback.print_exc()
    return wrapper


def get_channel():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    return connection.channel()
