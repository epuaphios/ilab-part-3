from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


dag = DAG(
    'my_dag',
    schedule_interval='0 10 * * *',
    start_date=datetime(2023, 5, 29),
    catchup=False
)

t1 = BashOperator(
    task_id='dbt-1',
    bash_command='dbt run --models dbt-1 --projects_dir /opt/dbt/part3/profiles.yml',
    dag=dag)

t2 = BashOperator(
    task_id='dbt-2',
    bash_command='dbt run --models dbt-2 --projects_dir /opt/dbt/part3/profiles.yml',
    dag=dag)

t1 >> t2
