SELECT Fname, Minit, Lname
FROM k_employee
LEFT JOIN k_dependent ON Essn=Ssn
GROUP BY Ssn HAVING COUNT(Relationship)=0
ORDER BY Fname;