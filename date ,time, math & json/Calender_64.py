import calendar
import datetime
from calendar import monthrange

Today = datetime.date.today()
year = Today.year
month = Today.month
print(calendar.month(year, month))

first_date = datetime.date(year, month, 1)
n_days = monthrange(year, month)[1]
first_date = int((first_date.strftime("%w")))
if first_date == 0:
    sunday_1 = 1
    first_date = 7
else:
    sunday_1 = 8-first_date
print(first_date)
val = []

for i in range(0, 5):
    val.append(sunday_1)
    sunday_1 += 7
print(val)
D_t = datetime.datetime.now()
print('\t\t', D_t.strftime("%B"), end='')
print(D_t.year)
print("\tMo\tTu\tWe\tTh\tFr\tSa\tSu")
for i in range(1, n_days+1):
    if i in val:
        print('\t'*first_date, i, end='')
        print('\n')
    else:
        print('\t'*first_date, i, end='')
    first_date = 1
