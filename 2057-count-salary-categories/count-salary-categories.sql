# Write your MySQL query statement below
select 'Low Salary' as category,
count(case when a.income<20000 then 1 end) as accounts_count from accounts a
union all
select 'Average Salary' as category,
count(case when a.income between 20000 and 50000 then 1 end) as accounts_count from accounts a
union all
select 'High Salary' as category,
count(case when a.income>50000 then 1 end) as accounts_count from accounts a