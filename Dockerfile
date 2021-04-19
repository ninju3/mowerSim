FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONPATH "/app"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .