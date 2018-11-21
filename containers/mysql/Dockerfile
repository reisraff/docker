FROM mysql:5.7.20

ENV TERM=linux

RUN apt-get update \
    && apt-get -y install curl ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

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

RUN rm -rf /usr/local/bin/docker-entrypoint.sh \
    && rm -rf /entrypoint.sh

COPY ./docker-entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint.sh \
    && ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
