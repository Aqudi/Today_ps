SELECT Fname, Minit, Lname, Hours
FROM k_works_on
JOIN k_project ON Pno=Pnumber
JOIN k_employee ON Ssn=Essn
WHERE Pname='ProductX' AND Hours>=10;