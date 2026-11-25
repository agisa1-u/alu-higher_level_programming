-- Lists the cities of California using a subquery, sorted by cities.id
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
