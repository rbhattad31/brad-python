import calendar
from datetime import date

print(calendar.month(2022, 6))

today_s_date = date.today()

print("Current month:", today_s_date.month)
print('\n')

if today_s_date.month == 6:

    June0 = [['+++++++', 'J', 'U', 'N', 'E', '+++++++']]
    June1 = [['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']]
    June2 = [['  ', '  ', ' 1', ' 2', ' 3', ' 4', ' 5']]
    June3 = [[' 6', ' 7', ' 8', ' 9', '10', '11', '12']]
    June4 = [['13', '14', '15', '16', '17', '18', '19']]
    June5 = [['20', '21', '22', '23', '24', '25', '26']]
    June6 = [['27', '28', '29', '30', '  ', '  ', '  ']]

    print(June0)
    print(June1)
    print(June2)
    print(June3)
    print(June4)
    print(June5)
    print(June6)
