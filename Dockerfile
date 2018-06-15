FROM node:latest

RUN apt-get update && apt-get install -y libfreetype6 libfontconfig xfonts-75dpi xfonts-base

RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.jessie_amd64.deb \
    && dpkg -i wkhtmltox_0.12.5-1.jessie_amd64.deb \
    && rm -f wkhtmltox_0.12.5-1.jessie_amd64.deb


ADD ./Fonts/muli /usr/share/fonts/truetype/muli
RUN fc-cache -fv

WORKDIR /ka
COPY package.json /ka
RUN npm install
