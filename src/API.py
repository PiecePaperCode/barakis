import json
from flask import Flask, jsonify, request
from bot import add, remove, active

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({'response': 'This is the Barakis API'})


@app.route("/start", methods=['POST'])
def start():
    response = json.loads(request.data)
    if add(
        response['universe'],
        response['username'],
        response['password']
    ):
        return jsonify({'response': True})
    else:
        return jsonify({'response': False})


@app.route("/remove", methods=['POST'])
def stop():
    response = json.loads(request.data)
    if remove(
        response['universe'],
        response['username']
    ):
        return jsonify({'response': True})
    else:
        return jsonify({'response': False})


@app.route("/active", methods=['POST'])
def running():
    response = json.loads(request.data)
    if active(
        response['universe'],
        response['username']
    ):
        return jsonify({'response': True})
    else:
        return jsonify({'response': False})
