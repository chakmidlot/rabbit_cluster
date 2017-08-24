import pika
import time

from backend.utils import reconnect, get_channel


i = 0

@reconnect
def send():
    global i

    channel = get_channel()

    channel.queue_declare(queue='hello')

    while True:
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=str(i))

        print(f"Sent '{i}'")

        i += 1


if __name__ == '__main__':
    send()
