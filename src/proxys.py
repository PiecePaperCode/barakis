import random
import requests


def random_proxy() -> str:
    proxy = requests.get(
        url=''
    ).text.split('\r\n')
    proxy = [text.split(':') for text in proxy]
    active = proxy[random.randint(0, 99)]
    proxy = 'socks5://{}:{}@{}:{}'.format(
           active[2], active[3], active[0], active[1]
    )
    return proxy
