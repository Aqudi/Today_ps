SELECT Fname, Minit, Lname, COUNT(Relationship)
FROM k_employee 
JOIN k_dependent ON Ssn=Essn
GROUP BY Ssn;