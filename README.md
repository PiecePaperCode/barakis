# Barakis
<img src="https://github.com/alaingilbert/pyogame/blob/develop/logo.png?raw=true" width="300" alt="logo">
Advanced free to use Ogame Bot using the pyogame lib
This Bot is used in pyogame.net

## Install
```shell
git clone clone https://github.com/PiecePaperCode/barakis.git
cd barakis
pip install -r requirements.txt
```

## Start
```shell
cd src
python main.py
```
it starts the Rest API and the Scheduler and awaits bots

## How to Use
``` python
import requests

url = 'http://127.0.0.1:80/{}'

response = requests.get(url.format(''))
print(response.text)

response = requests.post(
    url.format('start'),
    json={
        'universe': UNI,
        'username': EMAIL,
        'password': PASSWORD
    }
)
print(response.json)

response = requests.post(
    url.format('active'),
    json={
        'universe': UNI,
        'username': EMAIL,
    }
)
print(response.json)

response = requests.post(
    url.format('remove'),
    json={
        'universe': UNI,
        'username': EMAIL,
    }
)
print(response.json)
```

## Deployement with Docker
This bot is used in an Docker enviroment as a microservice
configure bot.dockerfile and docker-compose.yml to your needs.

