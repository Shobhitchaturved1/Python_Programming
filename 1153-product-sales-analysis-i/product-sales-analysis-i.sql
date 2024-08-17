# Write your MySQL query statement below
select p.product_name as product_name,s.year as year,s.price as price
from product as p join sales as s where p.product_id=s.product_id