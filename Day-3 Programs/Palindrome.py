print("Enter the string")
str1=input()
half=int(len(str1) / 2)
if (str1 == str1[::-1]):
	print("palindrome")
else:
	print("Not palindrome")
if len(str1) % 2 == 0:
    first_str = str1[:half]
    second_str = str1[half:]
else:
    first_str = str1[:half]
    second_str = str1[half+1:]
if first_str == second_str:
    print(str1, 'string is symmertical')
else:
    print(str1, 'string is not symmertical')
