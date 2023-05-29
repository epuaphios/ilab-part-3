with dbt-1 as (
    select
    date_trunc('month', order_date) as month,
    product_id,
    count(order_id) as total_orders,
    sum(total_amount) as total_sales
from
   {{ ref('orders') }}
group by
    1, 2
    )

select
    m.month,
    m.product_id,
    p.product_category,
    m.total_orders,
    m.total_sales
from
    dbt-1 as m
        join {{ ref('products') }} as p on m.product_id = p.product_id
