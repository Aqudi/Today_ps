SELECT Fname, Minit, Lname from k_employee as ke join (
    select ssn
    from k_employee
    where Fname='Franklin' and Lname='Wong'
) as km on ke.super_ssn = km.ssn
order by ke.Fname;