FROM mysql:5.7.20

ENV TERM=linux

RUN apt-get update \
    && apt-get -y install curl ca-certificates sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* ~/.composer \
    && useradd -ms /bin/bash docker \
    && echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN rm -rf /usr/local/bin/docker-entrypoint.sh \
    && rm -rf /entrypoint.sh

COPY ./docker-entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint.sh \
    && ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
