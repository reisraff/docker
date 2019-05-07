FROM ubuntu:xenial

ENV TERM=linux

RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" > /etc/apt/sources.list.d/ondrej-php.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C \
    && apt-get update \
    && apt-get -y install git curl ca-certificates \
        php5.6 php5.6-phpdbg php5.6-bz2 php5.6-cli php5.6-common php5.6-curl php5.6-dev php5.6-dom php5.6-bcmath php5.6-fpm php5.6-gd php5.6-json php5.6-mbstring php5.6-mcrypt php5.6-pdo php5.6-pdo-mysql php5.6-pdo-pgsql php5.6-readline php5.6-redis php5.6-simplexml php5.6-soap php5.6-xml php5.6-zip \
        php7.3 php7.3-phpdbg php7.3-bz2 php7.3-cli php7.3-common php7.3-curl php7.3-dev php7.3-dom php7.3-bcmath php7.3-fpm php7.3-gd php7.3-json php7.3-mbstring               php7.3-pdo php7.3-pdo-mysql php7.3-pdo-pgsql php7.3-readline php7.3-redis php7.3-simplexml php7.3-soap php7.3-xml php7.3-zip \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* ~/.composer

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