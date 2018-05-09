FROM node:latest

RUN apt-get install -y libfreetype6 libfontconfig

WORKDIR /ka
COPY package.json /ka
RUN npm install
