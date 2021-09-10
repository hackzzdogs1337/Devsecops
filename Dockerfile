FROM httpd:latest
RUN apt update && apt upgrade -y \
    && DEBIAN_FRONTEND="noninteractive" apt install tzdata -y \
    && apt-get install python3-pip -y \
    && pip3 install django
COPY krakenweb/* /var/www/html/kraken

RUN chmod -R 777 /var/www/html/kraken \
    && chown www-data:www-data -R /var/www/html/kraken

EXPOSE 80/tcp



