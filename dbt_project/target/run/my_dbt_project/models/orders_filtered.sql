
  create or replace   view ANALYTICS.SCHEMA.orders_filtered
  
   as (
    SELECT
    order_id,
    customer_id,
    order_date,
    amount AS order_amount
FROM ANALYTICS.SCHEMA.raw_orders
WHERE amount > 100
  );

