-- Write your PostgreSQL query statement below
WITH sub AS (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
)

DELETE FROM Person
WHERE id NOT IN (SELECT * FROM sub);