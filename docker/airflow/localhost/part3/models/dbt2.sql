with dbt2 as (
    select
    month,
    product_category,
    sum(total_orders) as total_orders,
    sum(total_sales) as total_sales
from
    public.dbt1
group by
    1, 2
    )

select
    month,
    product_category,
    total_orders,
    total_sales
from
    dbt2
