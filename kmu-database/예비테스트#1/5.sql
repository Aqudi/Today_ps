select ke.Fname, ke.Minit, ke.Lname, ke.Sex, km.Fname, km.Minit, km.Lname, km.Sex
from k_employee as ke LEFT JOIN k_employee as km on km.ssn=ke.Super_ssn
order by ke.fname;