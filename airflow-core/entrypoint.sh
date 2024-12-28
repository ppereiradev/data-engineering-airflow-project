#!/bin/bash

# Ativa o ambiente virtual
source /home/venv/bin/activate

# Comando para iniciar os serviços necessários
airflow db migrate

# Verifica se o usuário admin já existe
airflow users list | grep "${AIRFLOW_ADMIN_USERNAME}" > /dev/null
if [ $? -ne 0 ]; then
  airflow users create \
    --role Admin \
    --username "${AIRFLOW_ADMIN_USERNAME}" \
    --email "${AIRFLOW_ADMIN_EMAIL}" \
    --firstname "${AIRFLOW_ADMIN_FIRSTNAME}" \
    --lastname "${AIRFLOW_ADMIN_LASTNAME}" \
    --password "${AIRFLOW_ADMIN_PASSWORD}"
fi

tail -f /dev/null  # Manter o conteiner ativo
