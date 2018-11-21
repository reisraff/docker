FROM ubuntu:xenial

ENV TERM=linux

RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" > /etc/apt/sources.list.d/ondrej-php.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C \
    && apt-get update \
    && apt-get -y install git curl ca-certificates \
        php5.6 php5.6-xdebug php5.6-bz2 php5.6-cli php5.6-common php5.6-curl php5.6-dev php5.6-dom php5.6-bcmath php5.6-fpm php5.6-gd php5.6-json php5.6-mbstring php5.6-mcrypt php5.6-pdo php5.6-pdo-mysql php5.6-readline php5.6-redis php5.6-simplexml php5.6-soap php5.6-xml php5.6-zip \
        php7.2 php7.2-xdebug php7.2-bz2 php7.2-cli php7.2-common php7.2-curl php7.2-dev php7.2-dom php7.2-bcmath php7.2-fpm php7.2-gd php7.2-json php7.2-mbstring               php7.2-pdo php7.2-pdo-mysql php7.2-readline php7.2-redis php7.2-simplexml php7.2-soap php7.2-xml php7.2-zip \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* ~/.composer

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