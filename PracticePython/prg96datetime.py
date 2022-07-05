import datetime
from datetime import datetime
print("Datetime object for Jan 11 2012:")
print(datetime(2012, 1, 11))
print("\nSpecific date and time of 9:20 pm")
print(datetime(2011, 1, 11, 21, 20))
print("\nLocal date and time:")
print(datetime.now())
print("\nA date without time: ")
print(datetime.date(datetime(2012, 5, 22)))
print("\nCurrent date:")
print(datetime.now().date())
print("\nTime from a datetime:")
print(datetime.time(datetime(2012, 12, 15, 18, 12)))
print("\nCurrent local time:")
print(datetime.now().time())