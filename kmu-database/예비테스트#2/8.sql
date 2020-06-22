SELECT Fname, Minit, Lname, (
    SELECT COUNT(*)
    FROM k_dependent 
    WHERE Ssn=Essn
)
FROM k_employee as ke 
JOIN k_dependent ON Ssn=Essn
WHERE Relationship in ('Son', 'Daughter')
GROUP BY Ssn
ORDER BY Fname;