FROM python:3.12.4-bullseye

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /work
