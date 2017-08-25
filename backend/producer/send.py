from backend.utils import reconnect, get_channel


class Sender:

    def __init__(self):
        self.channel = None

    def send(self, items):
        for item in items:
            self.send_message(item)

    def send_message(self, item):
        while True:
            try:
                while not self.channel.basic_publish(exchange='',
                                                     routing_key='hello',
                                                     body=item,
                                                     mandatory=True):
                    print("Resend")
                return

            except Exception:
                self.connect()
                print('Connected')

    def connect(self):
        self.channel = get_channel()
        self.channel.confirm_delivery()

        self.channel.queue_declare(queue='hello')


if __name__ == '__main__':
    Sender().send(['1', '2', '4'])
