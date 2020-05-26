FROM ubuntu:xenial

ENV TERM=linux

ARG PHP_VERSION

RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" > /etc/apt/sources.list.d/ondrej-php.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C \
    && apt-get update \
    && apt-get -y install git curl ca-certificates \
        php5.6 php5.6-phpdbg php5.6-bz2 php5.6-cli php5.6-common php5.6-curl php5.6-dev php5.6-dom php5.6-bcmath php5.6-fpm php5.6-gd php5.6-json php5.6-mbstring php5.6-mcrypt php5.6-pdo php5.6-pdo-mysql php5.6-pdo-pgsql php5.6-readline php5.6-redis php5.6-simplexml php5.6-soap php5.6-xml php5.6-zip \
        php$(echo $PHP_VERSION) php$(echo $PHP_VERSION)-phpdbg php$(echo $PHP_VERSION)-bz2 php$(echo $PHP_VERSION)-cli php$(echo $PHP_VERSION)-common php$(echo $PHP_VERSION)-curl php$(echo $PHP_VERSION)-dev php$(echo $PHP_VERSION)-dom php$(echo $PHP_VERSION)-bcmath php$(echo $PHP_VERSION)-fpm php$(echo $PHP_VERSION)-gd php$(echo $PHP_VERSION)-json php$(echo $PHP_VERSION)-mbstring               php$(echo $PHP_VERSION)-pdo php$(echo $PHP_VERSION)-pdo-mysql php$(echo $PHP_VERSION)-pdo-pgsql php$(echo $PHP_VERSION)-readline php$(echo $PHP_VERSION)-redis php$(echo $PHP_VERSION)-simplexml php$(echo $PHP_VERSION)-soap php$(echo $PHP_VERSION)-xml php$(echo $PHP_VERSION)-zip php-mongodb \
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