SELECT Count(*)
FROM k_employee 
JOIN k_dependent ON Ssn=Essn
WHERE Relationship='Spouse';