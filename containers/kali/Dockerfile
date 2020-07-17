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
