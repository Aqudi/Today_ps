SELECT Fname, Minit, Lname, COUNT(Relationship) as NOD
FROM k_employee
LEFT JOIN k_dependent ON Ssn=Essn
GROUP BY Ssn
ORDER BY NOD DESC, Fname;