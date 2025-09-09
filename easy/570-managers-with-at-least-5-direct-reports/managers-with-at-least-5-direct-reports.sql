-- Write your PostgreSQL query statement below
WITH reports AS (
    SELECT
        managerId,
        COUNT(managerId)
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
)

SELECT 
    name
FROM Employee
JOIN reports
ON Employee.id = reports.managerId
