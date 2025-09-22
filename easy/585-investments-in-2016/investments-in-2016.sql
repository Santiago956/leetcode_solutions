WITH past_tiv AS (
    SELECT 
        *
    FROM Insurance
    WHERE tiv_2015 IN (
        SELECT 
            tiv_2015
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(tiv_2015) > 1
    )
),
loc AS (
SELECT
    *
FROM Insurance
WHERE (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
    )
)

SELECT
    ROUND(SUM(p.tiv_2016::numeric),2) AS tiv_2016
FROM past_tiv p
JOIN loc l ON(p.pid = l.pid)
