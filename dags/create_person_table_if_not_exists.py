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
    dag_id="create_person_table_if_not_exists",
    default_args=default_args,
    schedule="@once",
    catchup=False,
) as dag:
    create_person_table = SQLExecuteQueryOperator(
        task_id="create_person_table",
        conn_id="warehouse-postgres",
        sql="sql/person_schema.sql",
    )
