import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'ppereira.dev',
    'start_date': dt.datetime(2024, 12, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'csv_to_sql',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),
    catchup=False
) as extraction_dag:
    print_starting = BashOperator(
        task_id='starting',
        bash_command='date && echo "I am reading the CSV now..."',
    )

    csv_to_json = BashOperator(
        task_id='converting',
        bash_command='python /airflow-core/scripts/data_extraction/csv_to_sql.py'
    )

    print_finishing = BashOperator(
        task_id='finishing',
        bash_command='date && echo "I am finishing now..."',
    )

    print_starting >> csv_to_json
    csv_to_json >> print_finishing
