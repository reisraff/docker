FROM ubuntu:xenial

ENV TERM=linux

RUN apt-get update \
    && apt-get -y install curl wget ca-certificates sudo \
        python2.7 python2.7-dev \
    # && wget -q -O- https://bootstrap.pypa.io/get-pip.py | python \
    && useradd -ms /bin/bash docker \
    && echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

COPY ./run.sh /home/docker/run.sh
RUN chmod +x /home/docker/run.sh

USER docker
WORKDIR /home/docker/
