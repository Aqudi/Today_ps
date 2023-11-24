select Fname, Minit, Lname, Salary * 1.1
from k_works_on
join k_employee on Ssn=Essn
join k_project on Pno=Pnumber
where Pname='ProductX';