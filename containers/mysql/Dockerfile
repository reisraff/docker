FROM debian:jessie

RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections
RUN apt-get update && apt-get install -y mysql-server mysql-client

RUN sed -i -e "s/127.0.0.1/0.0.0.0/g" /etc/mysql/my.cnf

RUN /etc/init.d/mysql start && \
sleep 5 && \
mysql -uroot -proot -e "CREATE USER 'root'@'%' IDENTIFIED BY 'root';" && \
mysql -uroot -proot -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;"

COPY ./run.sh /root/run.sh
RUN chmod +x /root/run.sh
