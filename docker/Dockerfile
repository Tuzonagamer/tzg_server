FROM python:3.7

ARG ssh_prv_key
ARG ssh_pub_key

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Bogota

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub

RUN apt-get update && \
    apt-get upgrade -y

RUN apt install -y tzdata

RUN pip install pip --upgrade  && \
    pip install paramiko && \
    pip install Flask && \
    pip install click==7.1.1 && \
    pip install Flask==1.1.1 && \
    pip install itsdangerous==1.1.0 && \
    pip install Jinja2==2.11.1 && \
    pip install MarkupSafe==1.1.1 && \
    pip install scramp==1.1.1 && \
    pip install Werkzeug==1.0.0 && \
    pip install six==1.14.0 && \
    pip install SQLAlchemy==1.3.16 && \
    pip install SQLAlchemy-Utils==0.36.3 && \
    pip install psycopg2-binary==2.8.5 && \
    pip install PyMySQL==0.9.3 && \
    pip install Flask-SQLAlchemy==2.4.1 && \
    pip install Unidecode && \
    pip install wheel && \
    pip install -U flask-cors && \
    pip install gunicorn

RUN echo "America/Bogota" > /etc/timezone
RUN mkdir /tzg_server
WORKDIR /tzg_server

#Permisos para gunicorn
#RUN chown -R flask:flaskgroup /metadataimagemicroservice
#USER flask

#gunicorn configuration
RUN pip install pytest==7.1.3 cerberus==1.3.4 


ENV FLASK_APP app/__init__.py
EXPOSE 5000
EXPOSE 5432
ENTRYPOINT [ "gunicorn", "-c", "gunicornconfig.py"]
CMD ["wsgi:app", "/tzg_server"]
