FROM kalilinux/kali-linux-docker:latest

RUN apt-get update && apt-get install kali-linux-all -y

RUN apt-get update \
    && apt-get -y install gcc-multilib exiftool git eog \
    && gem install zsteg \
    && wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar && chmod +x stegsolve.jar \
    && pip install pwn \
    && curl -s https://api.github.com/repos/sharkdp/bat/releases/latest \
          | grep browser_download_url \
          | grep 'bat_0.9.0_amd64.deb' \
          | cut -d '"' -f 4 \
          | wget -qi - \
    && dpkg -i *deb \
    && rm -f *deb

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
    && sudo -H -u $IMGUSER bash -c 'git clone https://github.com/longld/peda.git ~/peda' \
    && echo "DONE! debug your program with gdb and enjoy" \
    && echo "User $IMGUSER($IMGUID:$IMGGID) has been created"
