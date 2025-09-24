WITH qntd AS (
    SELECT 
        customer_number,
        COUNT(order_number) AS orders_qntd
    FROM Orders
    GROUP BY customer_number
    ORDER BY orders_qntd DESC
)

SELECT
    customer_number
FROM qntd
LIMIT 1;