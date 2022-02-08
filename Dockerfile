
# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/


RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip3 install psycopg2


RUN pip install -r requirements.txt
COPY . /code/
