
  
    

        create or replace transient table ANALYTICS.SCHEMA.stg_orders
         as
        (

WITH cleaned_data AS (
    SELECT
        ORDER_ID,
        CUSTOMER_ID,
        CUSTOMER_FNAME || ' ' || CUSTOMER_LNAME AS FULL_CUSTOMER_NAME,
        CUSTOMER_CITY,
        CUSTOMER_COUNTRY,
        CUSTOMER_SEGMENT,
        TRY_TO_DATE(ORDER_DATE, 'YYYY-MM-DD') AS ORDER_DATE, -- Convert ORDER_DATE to DATE
        TRY_TO_DATE(SHIPPING_DATE, 'YYYY-MM-DD') AS SHIPPING_DATE, -- Convert SHIPPING_DATE to DATE
        SALES,
        BENEFIT_PER_ORDER,
        LATE_DELIVERY_RISK,
        DELIVERY_STATUS
    FROM ANALYTICS.SCHEMA.DATA
    WHERE ORDER_ID IS NOT NULL -- Filter out rows with missing ORDER_ID
      AND CUSTOMER_ID IS NOT NULL -- Filter out rows with missing CUSTOMER_ID
)

SELECT *
FROM cleaned_data
        );
      
  