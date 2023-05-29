from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_dbt():
    command = 'dbt run --models dbt --data orders.csv,products.csv > dbt_output.txt'
    subprocess.run(command, shell=True)

def read_dbt_output():
    with open('dbt_output.txt', 'r') as file:
         output = file.read()
    print(output)

dag = DAG(
    'dbt_workflow',
    description='dbt iş akışı',
    start_date=datetime(2023, 5, 29),
    catchup=False
)

dbt_task = PythonOperator(
    task_id='run_dbt_task',
    python_callable=run_dbt,
    dag=dag
)
dbt_task2 = PythonOperator(
    task_id='run_dbt_task2',
    python_callable=read_dbt_output,
    dag=dag
)

dbt_task >> dbt_task2
