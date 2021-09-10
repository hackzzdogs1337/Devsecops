FROM httpd:latest
RUN apt update && apt upgrade -y \
    && DEBIAN_FRONTEND="noninteractive" apt install tzdata -y \
    && apt-get install apache2 libapache2-mod-wsgi-py3 python3-pip -y \
    && pip3 install pipenv django
COPY krakenweb /var/www/html/kraken

COPY config/kraken.conf /etc/apache2/sites-available/kraken.conf

RUN virtualenv /var/www/html/kraken/venv \
    && /bin/bash -c "source /var/www/html/kraken/venv/bin/activate && pip3 install django"

RUN chmod -R 777 /var/www/html/kraken \
    && chown www-data:www-data -R /var/www/html/kraken

EXPOSE 80/tcp

RUN a2dissite 000-default \
    && a2ensite kraken



