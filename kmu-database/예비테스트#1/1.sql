SELECT Dname, Fname, Minit, Lname, Pname
FROM k_employee
JOIN k_department on Dno=Dnumber
JOIN k_works_on on Ssn=Essn
JOIN k_project on Pno=Pnumber
ORDER BY Dname Desc, Fname, Pname;