from datetime import date


def calc_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


yy = int(input("Enter the year: "))
mm = int(input("Enter the month(in no): "))
dd = int(input("Enter the date: "))
print(calc_age(date(yy, mm, dd)), "years")
