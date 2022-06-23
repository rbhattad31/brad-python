def findAge(C_date, C_month, C_year,
            b_date, b_month, b_year):

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if b_date > C_date:
        C_month = C_month - 1
        C_date = C_date + month[b_month - 1]


    if b_month > C_month:
        C_year = C_year - 1
        C_month = C_month + 12

    # calculate date, month, year
    calculated_date = C_date - b_date
    calculated_month = C_month - b_month
    calculated_year = C_year - b_year

    # print present age
    print("Present Age: ")
    print("Years:", calculated_year, "Months:",
          calculated_month, "Days:", calculated_date)


# driver code
current_date = 6
current_month = 17
current_year = 2022

# birth dd//mm//yyyy
birth_date = 5
birth_month = 5
birth_year = 1995

findAge(current_date, current_month, current_year,
        birth_date, birth_month, birth_year)