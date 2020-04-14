## 2. Joining Three Tables ##

select
    i.track_id, 
    t.name track_name,
    m.name track_type, 
   i.unit_price, 
    i.quantity 
from invoice_line i 
INNER JOIN track t on t.track_id=i.track_id
INNER join media_type m on m.media_type_id=t.media_type_id 
 where i.invoice_id=4;

## 3. Joining More Than Three Tables ##

SELECT
    il.track_id,
    t.name track_name,
    a.name artist_name,
    mt.name track_type,
    il.unit_price,
    il.quantity
    
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN album al on al.album_id=t.album_id 
INNER JOIN artist a on a.artist_id=al.artist_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id 
WHERE il.invoice_id = 4;

## 4. Combining Multiple Joins with Subqueries ##

select 
    album,
    artist, 
    count(i.track_id) as tracks_purchased  
    from invoice_line i
INNER JOIN
(select 
    t.track_id,
    a.name artist, 
    al.title album from track t
INNER JOIN album al on al.album_id= t.album_id
INNER JOIN artist a on a.artist_id=al.artist_id) c on c.track_id=i.track_id 
group by album
ORDER by tracks_purchased DESC limit 5

## 5. Recursive Joins ##

SELECT
    e1.first_name ||" "|| e1. last_name employee_name,
    e1.title employee_title,
    e2.first_name ||" "|| e2. last_name supervisor_name,
    e2.title supervisor_title
 FROM employee e1
Left JOIN employee e2 on e1.reports_to = e2.employee_id ORDER by employee_name
;

## 6. Pattern Matching Using Like ##

SELECT 
    first_name, 
    last_name,
    phone 
from customer where first_name LIKE "%Belle%"


## 7. Generating Columns With The Case Statement ##

select c.first_name|| " "||c.last_name as customer_name, 
    COUNT(i.customer_id) As number_of_purchases,
    sum(i.total) As total_spent,
    CASE
        when sum(i.total)<40 THEN "small spender"
        when sum(i.total)>100 THEN "big spender"
        when sum(i.total)>=40 and sum(i.total)<=100 THEN "regular"
        END
        as customer_category
from invoice i INNER JOIN customer c
on i.customer_id=c.customer_id
GROUP by customer_name
order by customer_name;