-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- BETWEEN number_1 AND number_2 is to select a range.
-- LIMIT to define the number of city to be printed
SELECT city, AVG(value) as avg_temp FROM temperatures  WHERE month BETWEEN 7 AND 8  GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
