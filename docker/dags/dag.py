from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}

dag = DAG(
    'dbt_dag', default_args=default_args, schedule_interval=timedelta(1), schedule="@continuous", max_active_runs=1,
    catchup=False,
)

t1 = BashOperator(
    task_id='dbt-1',
    bash_command='dbt run --models dbt-1',
    dag=dag)

t2 = BashOperator(
    task_id='dbt-2',
    bash_command='dbt run --models dbt-2',
    dag=dag)

t1 >> t2
