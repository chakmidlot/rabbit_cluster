from backend.utils import reconnect, get_channel


results = open('data.txt', 'ab')


def callback(ch, method, properties, body):
    results.write(body + b'\n')
    ch.basic_ack(delivery_tag=method.delivery_tag)


@reconnect
def read():
    channel = get_channel()
    channel.queue_declare(queue='hello')

    channel.basic_consume(callback, queue='hello')

    channel.start_consuming()


if __name__ == '__main__':
    read()
