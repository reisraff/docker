FROM kalilinux/kali-rolling:latest

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get -y install iputils-ping vim netcat iproute2 net-tools watch mlocate build-essential metasploit-framework gcc-multilib exiftool git eog gobuster python2.7 python2.7-dev python3-dev python3-pip \
    && curl https://bootstrap.pypa.io/get-pip.py | python2.7 \
    && ln -s /usr/bin/python2.7 /usr/bin/python2 \
    && pip install pwn requests \
    && pip3 install pwn requests

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
    && sudo -H -u $IMGUSER bash -c 'wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh' \
    && sudo -H -u $IMGUSER bash -c 'echo "" >> ~/.bashrc && echo "# GEF needing" >> ~/.bashrc && echo "export LC_CTYPE=C.UTF-8" >> ~/.bashrc && echo "" >> ~/.bashrc' \
    && echo "DONE! debug your program with gdb (GEF) and enjoy" \
    && echo "User $IMGUSER($IMGUID:$IMGGID) has been created"
