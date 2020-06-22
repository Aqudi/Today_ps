SELECT Fname, Minit, Lname,Relationship, Dependent_name
FROM k_employee
LEFT JOIN k_dependent ON Ssn=Essn
ORDER BY Fname, Minit, Lname;