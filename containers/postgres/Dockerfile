FROM postgres

ENV TERM=linux

ARG PY_VERSION

RUN apt-get update \
    && apt-get -y install curl ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

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