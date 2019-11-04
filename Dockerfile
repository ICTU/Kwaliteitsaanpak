FROM python:3.6-alpine

RUN apk --no-cache add make docker nodejs nodejs-npm libxml2-dev libxslt-dev libffi-dev gcc musl-dev bash openssl-dev

ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /ka
COPY package.json /ka
RUN npm install
