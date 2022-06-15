import random
import array

Password_Length = int(input('Enter the length of the password:'))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lower_case_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_case_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

combined_list = numbers + lower_case_characters + upper_case_characters + symbols

random_digit = random.choice(numbers)
random_upper = random.choice(upper_case_characters)
random_lower = random.choice(lower_case_characters)
random_symbol = random.choice(symbols)

temporary_password = random_digit + random_upper + random_lower + random_symbol

for x in range(Password_Length - 4):
    temporary_password = temporary_password + random.choice(combined_list)

    temporary_password_list = array.array('u', temporary_password)
    random.shuffle(temporary_password_list)

password = ""
for x in temporary_password_list:
    password = password + x

print(password)
