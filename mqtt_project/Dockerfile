FROM python:3.11-alpine3.17

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /django
WORKDIR /django

COPY ./requirements.txt /django/
RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /django/

