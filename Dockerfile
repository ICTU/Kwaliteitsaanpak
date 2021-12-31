FROM python:3.10.1-buster

RUN apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y --no-install-recommends make docker.io docker-compose ghostscript \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /work
