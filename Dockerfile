FROM python:3.10.1-buster

RUN apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y --no-install-recommends fontconfig libjpeg62-turbo libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base wget \
  && apt-get install -y --no-install-recommends make docker.io docker-compose ghostscript \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ARG ARCH

RUN wget --quiet https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_${ARCH}.deb \
    && dpkg -i wkhtmltox_0.12.6-1.buster_${ARCH}.deb \
    && rm -f wkhtmltox_0.12.6-1.buster_${ARCH}.deb

ADD ./thirdparty/fonts/muli /usr/share/fonts/truetype/muli
RUN fc-cache -fv

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /work
