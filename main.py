"""Simple REST API to test service mesh functionality."""
import json
import os

import requests
from flask import Flask

app = Flask(__name__)

def get_env():
    """Construct dictionary with Environmental Variables."""
    info = {}
    info['app_name'] = os.getenv('APP_NAME')
    info['version'] = os.getenv('VERSION')
    info['namespace'] = os.getenv('NAMESPACE')
    info['pod'] = os.getenv('POD')
    info['node'] = os.getenv('NODE')
    info['connect_url'] = os.getenv('CONNECT_URL')
    return info

def configure_routes(app, info):
    """Create router."""
    @app.route("/")
    def hello_world():
        return f"Hello from {info['app_name']}"

    @app.route("/info")
    def get_info():
        return json.dumps(info)

    @app.route("/connect")
    def connect():
        response = {}
        response['action'] = f"Connecting from {info['app_name']} to {info['connect_url']}"
        try:
            r = requests.get(url = info['connect_url'])
            response['response'] = str(r.content)
            response['code'] = r.status_code
        except requests.exceptions.ConnectionError as e:
            response['error'] = str(e.args[0].reason)
        return json.dumps(response)

configure_routes(app, get_env())

if __name__ == '__main__':
    app.run()