-- Displays maxt temperature of each state
-- Ordered by state

SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state ORDER BY state;
