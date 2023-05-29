FROM python:3.8

RUN pip install dbt
RUN pip install postgres-dbt
RUN dbt init --profiles-dir ./

COPY . /dbt
WORKDIR /dbt

CMD ["dbt", "run"]
