-- Import in hbtn_0c_0 database temperatures.sql
-- Computes then displays average temperature by city ordered by temp(desc)

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
