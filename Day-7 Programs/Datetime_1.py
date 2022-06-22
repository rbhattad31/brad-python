import datetime
# Print Date with time
D_t = datetime.datetime.now()
print(D_t)
# Print year
print(D_t.year)
# use strftime function
# print current day
print(D_t.strftime("%A"))
# print current short day
print(D_t.strftime("%a"))
# print Day of month
print(D_t.strftime("%d"))
# print Month name
print(D_t.strftime("%B"))
# print Hour
print(D_t.strftime("%H"))
# print AM/PM
print(D_t.strftime("%p"))
# Print century
print(D_t.strftime("%C"))
