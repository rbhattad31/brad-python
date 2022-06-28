import datetime

from datetime import date

x = datetime.datetime.now()
print(x)

print(datetime.datetime.now().year)

print(x.year)

print(x.strftime("%A"))

min_date = date.min
print("Min Date supported", min_date)

# Getting max date
max_date = date.max
print("Max Date supported", max_date)

Date = date(2020, 12, 11)

# Accessing the attributes
print("Year:", Date.year)
print("Month:", Date.month)
print("Day:", Date.day)

today = date.today()

print("Today's date is", today)

print("Weekday using weekday():", today.weekday())

# Getting Weekday
# method
print("Weekday:", today.isoweekday())

# Getting the Proleptic Gregorian
# ordinal
print("Proleptic Gregorian ordinal:", today.toordinal())

# Getting the date from the ordinal
print("Date from ordinal", date.fromordinal(737000))
