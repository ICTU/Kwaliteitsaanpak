FROM python:3.8-slim-buster

RUN lxml_run_time_deps='libxml2-dev libxslt-dev' \
  && apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y --no-install-recommends npm docker.io docker-compose $lxml_run_time_deps \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /work
COPY package.json /work
RUN npm install
