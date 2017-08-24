from multiprocessing import Process
import os

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return f"PID = {os.getpid()}"


if __name__ == '__main__':
    servers = [Process(target=app.run,
                       kwargs={'host': '0.0.0.0', 'port': port})
               for port in range(5001, 5004)]

    for server in servers:
        server.start()

    for server in servers:
        server.join()
