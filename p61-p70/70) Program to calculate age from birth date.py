from datetime import date


def calculate_age(birthdate):
    days_in_year = 365
    age = int((date.today() - birthdate).days / days_in_year)
    return age


print(calculate_age(date(1996, 9, 10)), "years")
