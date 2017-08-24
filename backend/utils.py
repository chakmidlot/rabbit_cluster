import traceback

import pika
from pika.exceptions import ConnectionClosed


def reconnect(func):
    def wrapper():
        while True:
            try:
                func()
            except ConnectionClosed:
                traceback.print_exc()
    return wrapper


def get_channel():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    return connection.channel()
