from threading import Thread
from bot import scheduler
from API import app
from waitress import serve

import socket
import redis


redis = redis.Redis(
    host='barakis_redis',
    port=6379
)
hostname = socket.gethostname()


if __name__ == '__main__':
    BOT = Thread(target=scheduler)
    API = Thread(target=lambda: serve(app, host='0.0.0.0', port=8888))
    BOT.start()
    API.start()
    BOT.join()
    API.join()

