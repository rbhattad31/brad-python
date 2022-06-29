import datetime as dt

date_of_birth = dt.datetime(1999,7,4)
present_date = dt.datetime.now()
age =  present_date - date_of_birth
print(age)