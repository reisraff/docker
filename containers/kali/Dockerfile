FROM kalilinux/kali-linux-docker:latest

RUN apt-get update && apt-get install kali-linux-all -y

RUN apt-get update \
    && apt-get -y install gcc-multilib exiftool git eog gobuster \
    && gem install zsteg \
    && wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar && chmod +x stegsolve.jar \
    && pip install pwn \
    && wget https://www.ghidra-sre.org/ghidra_9.0.4_PUBLIC_20190516.zip \
    && unzip ghidra*.zip \
    && rm -rf ghidra*.zip \
    && sudo mv $(ls ./ | grep ghidra) /opt/ghidra \
    && echo -e '\nexport PATH=$PATH:/opt/ghidra/\n' | sudo tee -a /etc/bash.bashrc \
    && echo -e '#!/bin/bash\n\nghidraRun 2>&1 &' | sudo tee /usr/bin/ghidra \
    && sudo chmod +x /usr/bin/ghidra \
    && wget $(curl --silent "https://api.github.com/repos/sharkdp/bat/releases/latest" | grep -E 'url.+amd64.+deb' | grep -v musl | sed -r 's/.+(http[^"]+)"/\1/') && sudo dpkg -i ./*.deb

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
    # && sudo -H -u $IMGUSER bash -c 'git clone https://github.com/longld/peda.git ~/peda' \
    # && sudo -H -u $IMGUSER bash -c 'echo "source ~/peda/peda.py" >> ~/.gdbinit' \
    && sudo -H -u $IMGUSER bash -c 'wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh' \
    && sudo -H -u $IMGUSER bash -c 'echo "" >> ~/.bashrc && echo "# GEF needing" >> ~/.bashrc && echo "export LC_CTYPE=C.UTF-8" >> ~/.bashrc && echo "" >> ~/.bashrc' \
    && echo "DONE! debug your program with gdb (GEF) and enjoy" \
    && echo "User $IMGUSER($IMGUID:$IMGGID) has been created"
