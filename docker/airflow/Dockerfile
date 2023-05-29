FROM apache/airflow:2.1.0-python3.8

RUN pip install dbt

COPY ./dags /opt/airflow/dags

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

CMD ["webserver"]
