WITH first_login AS (
    SELECT 
        player_id,
        MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),
next_day_login AS (
    SELECT
        f.player_id
    FROM first_login AS f
    JOIN Activity AS a
        ON f.player_id = a.player_id
        AND a.event_date = f.first_login_date + INTERVAL '1 day'
)

SELECT 
    ROUND(
        COUNT(DISTINCT n.player_id)*1.0/COUNT(f.player_id)
        , 2
    ) AS fraction
FROM first_login AS f
LEFT JOIN next_day_login AS n
    USING(player_id)