"""Simple REST API to test service mesh functionality."""
import json
import os

import requests
from flask import Flask

REQUEST_TIMEOUT = 20
INFO = {
    'app_name': os.getenv('APP_NAME'),
    'version': os.getenv('VERSION'),
    'namespace': os.getenv('NAMESPACE'),
    'pod': os.getenv('POD'),
    'node': os.getenv('NODE'),
    'connect_url': os.getenv('CONNECT_URL'),
}

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Define main route."""
    return f"Hello from {INFO['app_name']}"


@app.route("/info")
def get_info():
    """Info route."""
    return json.dumps(INFO)


@app.route("/connect")
def connect():
    """Connect with a external service."""
    response = {}
    response['action'] = f"Connecting from {INFO['app_name']} to {INFO['connect_url']}"
    try:
        request = requests.get(url=INFO['connect_url'], timeout=REQUEST_TIMEOUT)
        response['response'] = request.text
        response['code'] = request.status_code
    except requests.exceptions.ConnectionError as exc:
        response['error'] = str(exc.args[0].reason)
    return json.dumps(response)


if __name__ == '__main__':
    app.run()
