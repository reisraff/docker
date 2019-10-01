FROM ubuntu:xenial

ENV TERM=linux

ARG NODE_VERSION

RUN apt-get update \
    && apt-get -y install curl ca-certificates git sudo build-essential \
    && curl -sL https://deb.nodesource.com/setup_$(echo $NODE_VERSION).x | sudo -E bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* \
    && npm install --global yarn bower gulp gulp-cli \
    && echo fs.inotify.max_user_watches=524288 | tee -a /etc/sysctl.conf && sysctl -p

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
    && sudo -H -u $IMGUSER bash -c 'mkdir ~/.npm && sudo chown -R $(whoami) ~/.npm' \
    && echo "User $IMGUSER($IMGUID:$IMGGID) has been created"
