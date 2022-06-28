import calendar

yy = 2022
mm = 10

# display the calendar
print(calendar.month(yy, mm))

print("The calendar of the year  2022 is : ")
print(calendar.calendar(2022, 2, 1, 6))

obj = calendar.Calendar(firstweekday=0)
# of iterweekdays() method
for day in obj.iterweekdays():
    print(day)


obj = calendar.Calendar(firstweekday=5)
# iterating with itermonthdates
for day in obj.itermonthdates(2018, 4):
    print(day)