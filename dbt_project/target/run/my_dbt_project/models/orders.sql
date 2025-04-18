
  create or replace   view ANALYTICS.SCHEMA.orders
  
   as (
    -- models/stg_orders.sql

select
    order_id,
    customer_id,
    order_date,
    amount
from ANALYTICS.SCHEMA.raw_orders
  );

