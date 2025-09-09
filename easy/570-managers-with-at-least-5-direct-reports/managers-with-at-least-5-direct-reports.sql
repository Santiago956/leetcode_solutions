-- Write your PostgreSQL query statement below
SELECT 
    e.name
FROM Employee AS e
JOIN Employee AS sub
ON e.id = sub.managerId
GROUP BY e.id, e.name
HAVING COUNT(sub.id) >= 5