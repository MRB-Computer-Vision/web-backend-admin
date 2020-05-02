FROM python:3.8

LABEL APP="python"

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
COPY ./requirements_dev.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements_dev.txt

ENV PYTHONUNBUFFERED 1