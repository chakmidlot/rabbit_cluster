import pika
import time

from backend.utils import reconnect, get_channel


i = 0

@reconnect
def send():
    global i

    channel = get_channel()
    channel.confirm_delivery()

    channel.queue_declare(queue='hello')

    while True:
        try:
            sent = channel.basic_publish(exchange='',
                                         routing_key='hello',
                                         body=str(i),
                                         mandatory=True)
        except Exception:
            print(f"Failed: {i}")
            raise

        if sent:
            i += 1
        else:
            print(f"Didn't send: {i}")


if __name__ == '__main__':
    send()
