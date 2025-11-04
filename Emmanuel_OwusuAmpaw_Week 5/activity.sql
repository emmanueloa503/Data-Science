# Write your MySQL query statement below
SELECT 
    ROUND(AVG(a2.player_id IS NOT NULL), 2) AS fraction
FROM (
    SELECT 
        player_id, 
        MIN(event_date) AS first_day
    FROM Activity
    GROUP BY player_id
) AS f
LEFT JOIN Activity AS a2
ON 
    f.player_id = a2.player_id
    AND a2.event_date = DATE_ADD(f.first_day, INTERVAL 1 DAY);