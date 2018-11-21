FROM ubuntu:xenial

ENV TERM=linux

RUN apt-get update \
    && apt-get -y install curl ca-certificates sudo \
    && curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* \
    && npm install --global bower gulp gulp-cli \
    && echo fs.inotify.max_user_watches=524288 | tee -a /etc/sysctl.conf && sysctl -p

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
    && sudo -H -u $C_USER bash -c 'mkdir ~/.npm && sudo chown -R $(whoami) ~/.npm' \
    && echo "User $C_USER has been created"
