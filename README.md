# simplerest
Simple REST API on Python

## Intro
The goal of this app is to test connections between different services running on Kubernetes on a service mesh.

## To Do
- Add How to deploy to kubernetes
- Add Istio tests and How to
- Add Consul tests and How to
- Add Cillium tests and How to

## CI/CD
![Tests and Builds](https://github.com/anevigat/simplerest/actions/workflows/simplerest.yml/badge.svg)
- On pull request: Tox testing (flake8,pylint,isort,pydocstyle,coverage) will run
- On pull request: A vulnerability scan will be perfomed on the created image.
- On push to main: A Docker image will be pushed automatically to Docker Hub: https://hub.docker.com/r/anevigat/simplerest

## How to use this repo locally: *to be complete*

### Start server A
```bash
APP_NAME="serviceA" VERSION="1.0.0" NAMESPACE="default" POD="serviceApod" NODE="node1" CONNECT_URL="http://127.0.0.1:5001/" flask --app main run --port 5000
```

### Start server B
```bash
APP_NAME="serviceB" VERSION="1.0.0" NAMESPACE="default" POD="serviceBpod" NODE="node2" CONNECT_URL="http://127.0.0.1:5000/" flask --app main run --port 5001
```

### Test service A
```bash
curl http://127.0.0.1:5000
Hello from serviceA%
```

### Test service B
```bash
curl http://127.0.0.1:5001
Hello from serviceB%
```

### Get service A info
```bash
curl http://127.0.0.1:5000/info
{"appName": "serviceA", "version": "1.0.0", "namespace": "default", "pod": "serviceApod", "node": "node1"}%
```

### Connect service A with service B
```bash
curl http://127.0.0.1:5000/connect
{"action": "Connecting to http://127.0.0.1:5001/", "response": "b'Hello from serviceB'", "code": 200}%
```


### App Example taken from:
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/