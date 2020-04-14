## 1. Introducing Joins ##

SELECT * from facts a INNER join cities b on a.id = b.facts_id limit 10

## 2. Understanding Inner Joins ##

SELECT b.*, a.name as country_name from facts a INNER join cities b on a.id = b.facts_id limit 5

## 4. Left Joins ##

SELECT f.name country, f.population  from facts f left join cities c on c.facts_id=f.id where c.name is null;

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name capital_city, f.name country, c.population from cities c INNER join facts f on c.facts_id=f.id where capital=1 order by 3 DESC limit 10


## 7. Combining Joins with Subqueries ##

select c.name capital_city, facts.name country, c.population from facts INNER JOIN (select * from cities where capital=1 and population>10000000) c on c.facts_id=facts.id ORDER by 3 DESC

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT
    f.name country,
    c.urban_pop,
    f.population total_pop,
    (c.urban_pop / CAST(f.population AS FLOAT)) urban_pct
FROM facts f
INNER JOIN (
            SELECT
                facts_id,
                SUM(population) urban_pop
            FROM cities
            GROUP BY 1
           ) c ON c.facts_id = f.id
WHERE urban_pct > .5
ORDER BY 4 ASC;