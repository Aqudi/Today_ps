select Pnumber, Dnum, Fname, Minit, Lname  
from k_project join (
    select Dnumber, Fname, Minit, Lname, ssn, mgr_ssn
    from k_department join k_employee on Mgr_ssn = ssn
) as k_deee on Dnumber=Dnum
where Plocation='Stafford';
