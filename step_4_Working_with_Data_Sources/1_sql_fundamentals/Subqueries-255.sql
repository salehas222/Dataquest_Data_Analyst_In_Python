## 2. Subqueries ##

SELECT Major, Unemployment_rate FROM recent_grads where Unemployment_rate < (SELECT AVG(Unemployment_rate) FROM recent_grads ) ORDER BY Unemployment_rate

## 3. Subquery In SELECT ##

SELECT CAST(COUNT(ShareWomen) as float)/(SELECT CAST(COUNT(*) AS float) FROM recent_grads) as "proportion_abv_avg" FROM recent_grads WHERE ShareWomen> (SELECT AVG(ShareWomen) FROM recent_grads)

## 4. Returning Multiple Results In Subqueries ##

SELECT  Major, major_category FROM recent_grads
where major_category IN 
(SELECT Major_category FROM recent_grads GROUP BY Major_category ORDER BY SUM(Total) DESC LIMIT 5)

## 5. Building Complex Subqueries ##

SELECT AVG(CAST(sample_size AS FLOAT)/CAST(total AS float))  as avg_ratio from recent_grads

## 6. Practice Integrating A Subquery With The Outer Query ##

SELECT Major, Major_category, CAST(sample_size AS FLOAT)/CAST(total AS float)  as ratio from recent_grads where ratio > (
SELECT AVG(CAST(sample_size AS FLOAT)/CAST(total AS float)) from recent_grads)