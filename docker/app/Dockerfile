# pull image
FROM python:3.8-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# upgrade pip
RUN pip install --upgrade pip wheel

# fix for backports.zoneinfo
RUN apt-get update
RUN apt-get -y install libpq-dev gcc


# install dependencies
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt


# copy source code
COPY ./app /usr/src/app