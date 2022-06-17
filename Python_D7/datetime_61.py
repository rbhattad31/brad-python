import datetime
import pytz

d = datetime.date(2012, 11, 10)
print(d)

# getting today date

td = datetime.date.today()
print("Today date is :", td)

print(td.weekday())
print(td.isoweekday())

tde = datetime.timedelta(days=7)
print(td + tde)
print(td - tde)

bday = datetime.date.today()
till_date = datetime.date(1997, 6, 11)
age = bday-till_date
print("you are", age.days, "Days old")

# to print the date

t = datetime.time(9, 22, 56,100000)
print(t)

# print date ,time together

dt = datetime.datetime(1997, 6, 11, 4, 5, 55,100000)
print(dt)

timed = datetime.timedelta(hours=12)

print(dt + timed)

# printing Different times
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

t1 = datetime.datetime(2012, 11, 10, 9, 25, 45, tzinfo=pytz.UTC)
print(t1)

t1_now = datetime.datetime.now(tz=pytz.UTC)
print(t1_now)
