FROM node:latest

RUN apt-get install -y libfreetype6 libfontconfig
RUN apt-get install -y wget

ENV PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
#COPY $PHANTOM_JS.tar.bz2 .

#RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
#example RUN wget -q https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2

#RUN tar xjf $PHANTOM_JS.tar.bz2
#RUN install -t /usr/local/bin $PHANTOM_JS/bin/phantomjs
#RUN rm -rf $PHANTOM_JS
#RUN rm $PHANTOM_JS.tar.bz2

WORKDIR /ka
COPY package.json /ka
RUN npm install

