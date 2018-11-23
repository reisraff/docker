FROM ubuntu:xenial

ENV TERM=linux

ARG PY_VERSION

RUN export PY_VERSION=$PY_VERSION && apt-get update \
    && apt-get -y install curl build-essential wget ca-certificates sudo \
        python$(echo $PY_VERSION) python$(echo $PY_VERSION)-dev \
    && ln -s /usr/bin/python$(echo $PY_VERSION) /usr/bin/python \
    && wget -q -O- https://bootstrap.pypa.io/get-pip.py | python

ARG USER
ARG UID
ARG GID
RUN export C_USER=$USER \
    && export C_UID=$UID \
    && export C_GID=$GID \
    && groupadd -g $C_GID $C_USER \
    && useradd -ms /bin/bash -u $C_UID -g $C_GID $C_USER \
    && apt-get update && apt-get install -y sudo \
    && echo "$C_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo "User $C_USER has been created"