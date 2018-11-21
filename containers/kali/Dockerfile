FROM kalilinux/kali-linux-docker:latest

RUN apt-get update && apt-get install kali-linux-all -y

RUN apt-get update \
    && apt-get -y install exiftool git eog \
    && gem install zsteg \
    && wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar && chmod +x stegsolve.jar \
    && pip install pwn

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
    && sudo -H -u $C_USER bash -c 'git clone https://github.com/longld/peda.git ~/peda' \
    && sudo -H -u $C_USER bash -c 'echo "source ~/peda/peda.py" >> ~/.gdbinit' \
    && echo "DONE! debug your program with gdb and enjoy" \
    && echo "User $C_USER has been created"
