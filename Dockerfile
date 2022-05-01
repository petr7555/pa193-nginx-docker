from ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install nginx python3 python3-pip -y
RUN pip install azure-cli azure-identity azure-keyvault-secrets azure-keyvault-certificates

COPY pa193-server.conf /etc/nginx/conf.d/
RUN mkdir -p /data

COPY download_cert.py /
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

CMD /entrypoint.sh
