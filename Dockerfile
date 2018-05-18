FROM node:latest

RUN apt-get install -y libfreetype6 libfontconfig

ADD ./Fonts/muli /usr/share/fonts/truetype/muli
RUN fc-cache -fv

WORKDIR /ka
COPY package.json /ka
RUN npm install
