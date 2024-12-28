FROM ubuntu:24.04

WORKDIR /airflow-core

EXPOSE 8080
EXPOSE 8081

RUN apt-get update \
    && apt-get install -y python3.12 \
    && apt-get install -y python3-pip \
    && apt-get install -y python3-venv \
    && apt-get install -y libpq-dev \
    && apt-get install -y tzdata

COPY ./requirements.txt .

RUN python3 -m venv /home/venv \
    && . /home/venv/bin/activate \
    && pip install pip --upgrade \
    && pip install 'apache-airflow[postgres,celery]' \
    && pip install -r requirements.txt \
    && echo "source /home/venv/bin/activate" >> ~/.bashrc

COPY ./entrypoint.sh .

RUN chmod +x /airflow-core/entrypoint.sh

ENTRYPOINT ["/airflow-core/entrypoint.sh"]
