
FROM httpd:latest
RUN apt update && apt upgrade -y
RUN DEBIAN_FRONTEND="noninteractive" apt install tzdata -y
RUN apt-get install apache2 libapache2-mod-wsgi-py3 python3-pip -y

RUN pip3 install pipenv
COPY krakenweb /var/www/html/kraken
COPY config/kraken.conf /etc/apache2/sites-available/kraken.conf

RUN virtualenv /var/www/html/kraken/venv
RUN /bin/bash -c "source /var/www/html/kraken/venv/bin/activate && pip3 install django"

RUN chmod -R 777 /var/www/html/kraken
RUN chown www-data:www-data -R /var/www/html/kraken

EXPOSE 80/tcp

RUN a2dissite 000-default
RUN a2ensite kraken



