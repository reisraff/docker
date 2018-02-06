FROM ubuntu:xenial

ENV TERM=linux

RUN apt-get update \
    && apt-get -y install curl ca-certificates sudo \
    && curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* ~/.composer \
    && npm install --global bower gulp gulp-cli \
    && useradd -ms /bin/bash docker \
    && echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    && sudo -H -u docker bash -c 'mkdir ~/.npm && sudo chown -R $(whoami) ~/.npm' \
    && echo fs.inotify.max_user_watches=524288 | tee -a /etc/sysctl.conf && sysctl -p

COPY ./run.sh /home/docker/run.sh
RUN chmod +x /home/docker/run.sh

USER docker
WORKDIR /home/docker/
