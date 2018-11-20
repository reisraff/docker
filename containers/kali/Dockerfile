FROM kalilinux/kali-linux-docker:latest

RUN apt-get update && apt-get install kali-linux-all -y

RUN apt-get update && \
    apt-get install exiftool git eog && \
    gem install zsteg && \
    wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar && chmod +x stegsolve.jar && \
    pip install pwn && \
    git clone https://github.com/longld/peda.git ~/peda && \
    echo "source ~/peda/peda.py" >> ~/.gdbinit && \
    echo "DONE! debug your program with gdb and enjoy"
