from ubuntu:20.04

RUN apt-get update && apt-get install nginx python3 -y

COPY pa193-server.conf /etc/nginx/conf.d/
RUN mkdir -p /data

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

CMD /entrypoint.sh
