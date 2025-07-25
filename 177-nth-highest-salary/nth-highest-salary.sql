CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT
        CASE
            WHEN N < 1 THEN NULL
            WHEN (SELECT COUNT(DISTINCT e.salary) FROM Employee AS e) >= N
            THEN (SELECT DISTINCT e.salary FROM Employee AS e ORDER BY e.salary DESC LIMIT 1 OFFSET N - 1) 
            ELSE NULL
        END AS "getNthHighestSalary(N)"
    FROM Employee AS e
    LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;