# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -e .

CMD [ "python3", "-m" , "flask",  "--app", "main", "run", "--host=0.0.0.0"]
