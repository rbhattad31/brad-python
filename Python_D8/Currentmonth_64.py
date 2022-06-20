import calendar
import datetime

year = int(input("Enter the year"))
month = int(input("Enter the month"))

myCal = calendar.month(year, month)
print(myCal)


current_month = datetime.datetime.now().strftime('%m')

print(current_month)
