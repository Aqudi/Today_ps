SELECT Fname, Minit, Lname, Address
from k_employee
where  Address LIKE '%Houston, TX%'
order by Fname;