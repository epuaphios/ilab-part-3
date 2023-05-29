FROM python:3.8

RUN pip install dbt

COPY . /dbt
WORKDIR /dbt

CMD ["dbt", "run"]
