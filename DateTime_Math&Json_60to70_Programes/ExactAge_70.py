from datetime import date


def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)

    # raised when birthdate is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year=today.year,
                                month=born.month + 1, day=1)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


# Driver code
print(calculateAge(date(1998, 9, 10)), "years")
