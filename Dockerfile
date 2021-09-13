FROM httpd:latest
RUN apt-get update \
    && DEBIAN_FRONTEND="noninteractive" apt install tzdata -y \
    && apt-get install python3-pip -y \
    && pip3 install django pillow
COPY krakenweb /var/www/html/kraken/

EXPOSE 8000

WORKDIR /var/www/html/kraken/

RUN python3 manage.py collectstatic 

ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]