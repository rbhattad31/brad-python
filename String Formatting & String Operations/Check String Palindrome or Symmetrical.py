string = input("Enter String Name: ")
half_string = int(len(string) / 2)

if len(string) % 2 == 0:  # even
    first_str = string[:half_string]
    second_str = string[half_string:]
else:  # odd
    first_str = string[:half_string]
    second_str = string[half_string + 1:]

# symmetric
if first_str == second_str:
    print('string is symmertical')
else:
    print('string is not symmertical')

# palindrome
if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
    print('string is palindrome')
else:
    print('string is not palindrome')