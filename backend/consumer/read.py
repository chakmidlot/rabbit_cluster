from backend.utils import reconnect, get_channel


i = 0


def callback(ch, method, properties, body):
    global i

    data = int(body)
    if i + 1 != data:
        print(f"{i}, {data}")

    i = data
    ch.basic_ack(delivery_tag=method.delivery_tag)

@reconnect
def read():
    channel = get_channel()
    channel.queue_declare(queue='hello')

    channel.basic_consume(callback, queue='hello')

    channel.start_consuming()


if __name__ == '__main__':
    read()
