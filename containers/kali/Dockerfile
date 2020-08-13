FROM kalilinux/kali-rolling:latest

RUN apt-get update \
    && apt-get upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install dnsutils smbmap smbclient exploitdb ftp gdb git hashcat hashcat-utils hydra hydra-gtk impacket-scripts \
        iputils-arping john johnny metasploit-framework msfpc nasm ncat netcat-traditional nmap ollydbg \
        openssh-server p7zip-full seclists socat sqlmap tcpdump tor unar unrar vim wfuzz \
        windows-binaries windows-privesc-check winexe wireshark wordlists wpscan zip iputils-ping \
        netcat iproute2 net-tools watch mlocate build-essential metasploit-framework gcc-multilib exiftool \
        eog gobuster python2.7 python2.7-dev python3-dev python3-pip \
    && curl https://bootstrap.pypa.io/get-pip.py | python2.7 \
    && ln -s /usr/bin/python2.7 /usr/bin/python2 \
    && pip install pwn requests \
    && pip3 install pwn requests

RUN apt-get update && apt-get install -y software-properties-common \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F \
    && apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu focal main" \
    && apt update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y dirbuster openvpn firefox-esr libcanberra-gtk-module libcanberra-gtk3-module mesa-utils libgl1-mesa-glx \
    && export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/java/jdk-11.0.8+10/bin/ \
    && export JAVA_HOME=/opt/java/jdk-11.0.8+10/

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
