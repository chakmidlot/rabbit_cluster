import json
import traceback
from time import sleep

import requests

from backend.producer.send import Sender


def iter_comments():
        while True:
            response = requests.get('https://www.reddit.com/r/all/comments/.json?limit=100')

            parsed_json = json.loads(response.text)

            if parsed_json.get('error') == 429:
                print(response.text)
                sleep(1)
            else:
                print(len(parsed_json['data']['children']))
                for comment in parsed_json['data']['children']:
                    yield json.dumps(comment['data'])


if __name__ == '__main__':
    Sender().send(iter_comments())

