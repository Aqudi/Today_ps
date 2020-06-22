SELECT * from k_employee;
select * from k_department;

select ssn, dname
from k_employee cross join k_department
order by ssn, dname;