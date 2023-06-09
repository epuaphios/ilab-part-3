FROM apache/airflow:2.1.0-python3.8

RUN pip install --upgrade pip
RUN pip install dbt-postgres
RUN pip install jinja2


COPY ./profiles.yml /opt/dbt/profiles.yml

COPY ./dags /opt/airflow/dags
COPY ../postgres/sql /opt/airflow/sql

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

CMD ["webserver"]
