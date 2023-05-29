with dbt-2 as (
    select
    month,
    product_category,
    sum(total_orders) as total_orders,
    sum(total_sales) as total_sales
from
    dbt-1
group by
    1, 2
    )

select
    mcs.month,
    mcs.product_category,
    mcs.total_orders,
    mcs.total_sales
from
    dbt-2
