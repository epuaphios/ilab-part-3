import airflow.utils.dates
from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

args = {'owner': 'airflow'}
dag = DAG(
    dag_id="extract",
    default_args=args,
    schedule_interval=None,
    start_date=airflow.utils.dates.days_ago(1),
    catchup=False,
)
create_table_orders = PostgresOperator(
    task_id="create_table",
    postgres_conn_id="postgres_default",
    sql="sql/create_orders.sql",
    dag=dag
)
create_table_products = PostgresOperator(
    task_id="create_table_products",
    postgres_conn_id="postgres_default",
    sql="sql/create_products.sql",
    dag=dag
)
extract_data_orders = PostgresOperator(
    dag=dag,
    task_id="extract_data_orders",
    sql="sql/orders_load.sql",
    postgres_conn_id="postgres_default",

)
extract_data_products = PostgresOperator(
    dag=dag,
    task_id="extract_data_products",
    sql="sql/products_load.sql",
    postgres_conn_id="postgres_default",

)
create_table_orders >> create_table_products >> extract_data_orders >> extract_data_products
if __name__ == "__main__":
    dag.cli()