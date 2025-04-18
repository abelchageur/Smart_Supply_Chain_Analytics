SELECT
    order_id,
    customer_id,
    order_date,
    amount AS order_amount
FROM ANALYTICS.SCHEMA.raw_orders
WHERE amount > 100