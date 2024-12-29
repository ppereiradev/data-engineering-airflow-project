import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.sensors.external_task import ExternalTaskSensor


default_args = {
    'owner': 'ppereira.dev',
    'start_date': dt.datetime(2024, 12, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'populate_table',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),
    catchup=False
) as populate_dag:
    sensor_task = ExternalTaskSensor(
        task_id="sensor_task",
        external_dag_id="csv_to_sql",
        external_task_id="finishing",
        timeout=600,
        allowed_states=["success"],
        failed_states=["failed", "skipped"],
        mode="reschedule",
    )

    populate_person_table = SQLExecuteQueryOperator(
        task_id="populate_person_table",
        conn_id="warehouse-postgres",
        sql="sql/populate_person_table.sql",
    )

    sensor_task >> populate_person_table
