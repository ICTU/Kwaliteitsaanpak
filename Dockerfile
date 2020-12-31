FROM python:3.9.1-buster

RUN lxml_run_time_deps='libxml2-dev libxslt-dev' \
  && apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y --no-install-recommends make docker.io docker-compose ghostscript $lxml_run_time_deps \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /work
