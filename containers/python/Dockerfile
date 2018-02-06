FROM ubuntu:xenial

ENV TERM=linux

ARG PY_VERSION

RUN export PY_VERSION=$PY_VERSION && apt-get update \
    && apt-get -y install curl wget ca-certificates sudo \
        python$(echo $PY_VERSION) python$(echo $PY_VERSION)-dev \
    && ln -s /usr/bin/python$(echo $PY_VERSION) /usr/bin/python \
    && wget -q -O- https://bootstrap.pypa.io/get-pip.py | python \
    && useradd -ms /bin/bash docker \
    && echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

COPY ./run.sh /home/docker/run.sh
RUN chmod +x /home/docker/run.sh

USER docker
WORKDIR /home/docker/
