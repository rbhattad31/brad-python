string = 'kho-kho'
half = int(len(string) / 2)

if len(string) % 2 == 0:
    first_str = string[:half]
    second_str = string[half:]
else:
    first_str = string[:half]
    second_str = string[half + 1:]

if first_str == second_str:
    print(string, 'string is symmetrical')
else:
    print(string, 'string is not symmetrical')

str1 = 'skeeksroforskeeks'

str1 = str1.casefold()

rev_str1 = "".join(reversed(str1))

if str1 == rev_str1:
    print("palindrome")
else:
    print("not palindrome")
