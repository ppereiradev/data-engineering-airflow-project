import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


default_args = {
    'owner': 'ppereira.dev',
    'start_date': dt.datetime(2024, 12, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'populate_table',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as populate_dag:
    populate_person_table = SQLExecuteQueryOperator(
        task_id="populate_person_table",
        conn_id="warehouse-postgres",
        sql="sql/populate_person_table.sql",
    )
