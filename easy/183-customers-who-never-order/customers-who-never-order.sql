-- Write your PostgreSQL query statement below
SELECT c.name "Customers"
FROM Customers c
FULL OUTER JOIN Orders o
ON c.id = o.customerId
WHERE c.id IS NULL OR o.customerId IS NULL
