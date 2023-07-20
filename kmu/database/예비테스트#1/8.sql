-- 간단하게 두 개의 결과를 만들고 Union 해도 괜찮다.
Select distinct Pnumber
FROM k_project as kp
JOIN k_department as kd ON kp.Dnum=kd.Dnumber
JOIN (
    SELECT Pno, Lname, Ssn
    FROM k_employee as ke
    JOIN k_works_on as kw on kw.Essn=ke.Ssn
    WHERE ke.Lname='Wong'
) as ke ON ke.Ssn=kd.Mgr_ssn OR ke.Pno=kp.Pnumber
WHERE ke.Ssn=kd.Mgr_ssn OR ke.Pno=kp.Pnumber
order by kp.Pnumber;