SELECT Dname, Dlocation, Pname, Plocation
FROM k_department as d
JOIN k_dept_locations as l ON l.Dnumber=d.Dnumber
JOIN k_project  as p ON l.Dlocation=p.Plocation
WHERE p.Dnum=d.Dnumber
ORDER BY d.Dname, p.Pname;