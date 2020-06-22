SELECT Fname, Minit, Lname, Address
from k_employee join k_department on dnumber=dno
where dname='Research';