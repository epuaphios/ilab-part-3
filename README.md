# ilab-part-3

create table orders (
order_id int,
customer_id int,
product_id int,
order_date date,
total_amount float
);

COPY orders FROM '/tmp/orders.csv' DELIMITER ',' CSV HEADER;

create table products (
product_id int,
product_category varchar(50),
product_price float
);

docker cp /home/ogn/denemeler/big_data/part-3/data/products.csv 34a93:/tmp
docker cp /home/ogn/denemeler/big_data/part-3/data/orders.csv 34a93:/tmp
