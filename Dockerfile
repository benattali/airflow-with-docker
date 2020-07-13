FROM puckel/docker-airflow:1.10.9
MAINTAINER ben.attali@pagaya.com
USER root

RUN pip install -U pip
COPY requirements.txt requirements.txt
RUN pip install --no-cache -r requirements.txt