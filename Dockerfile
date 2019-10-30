FROM python:3.6-alpine3.7
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install psycopg2
RUN pip install django
RUN pip install channels
RUN pip install channels-redis
RUN mkdir /application
WORKDIR /application
ADD . /application/