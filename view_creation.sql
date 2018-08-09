CREATE VIEW day_requests AS (
SELECT date(time) as day, COUNT(*) as requests, COUNT(CASE WHEN status LIKE '4%' THEN 1 END) AS error
FROM log
GROUP BY day );