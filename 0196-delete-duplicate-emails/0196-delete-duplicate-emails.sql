# Write your MySQL query statement below
delete p1
from person p1
inner join person p2
on p1.email = p2.email
where p1.id > p2.id