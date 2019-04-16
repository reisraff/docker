FROM ubuntu:xenial

ENV TERM=linux

ARG PY_VERSION

RUN export PY_VERSION=$PY_VERSION && apt-get update \
    && apt-get -y install curl build-essential wget ca-certificates sudo \
        python$(echo $PY_VERSION) python$(echo $PY_VERSION)-dev \
    && ln -s /usr/bin/python$(echo $PY_VERSION) /usr/bin/python \
    && wget -q -O- https://bootstrap.pypa.io/get-pip.py | python

ARG HOSTUSER
ARG HOSTUID
ARG HOSTGID
RUN export IMGUSER=$HOSTUSER \
    && export IMGUID=$HOSTUID \
    && export IMGGID=$HOSTGID \
    && groupadd -g $IMGGID $IMGUSER \
    && useradd -ms /bin/bash -u $IMGUID -g $IMGGID $IMGUSER \
    && apt-get update && apt-get install -y sudo \
    && echo "$IMGUSER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo "User $IMGUSER($IMGUID:$IMGGID) has been created"