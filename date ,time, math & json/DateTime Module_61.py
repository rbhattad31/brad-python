import time
b = time.time()
print(b)
# convert time
print(time.ctime(b))
# local time
print(time.localtime())

# struct format
a = time.localtime()
c = time.mktime(a)
# converts local time format
print(time.asctime(a))

# returns our choice of writing date format
x = time.strftime("%d/%m/%Y")
print(x)

import datetime
# datetime constructor
print(datetime.datetime(2022,6,15,17,46,57,356))
# coverts to today date
print(datetime.datetime.today())
# access some particular time or date or year
v = datetime.datetime.now()
print(v.second)
