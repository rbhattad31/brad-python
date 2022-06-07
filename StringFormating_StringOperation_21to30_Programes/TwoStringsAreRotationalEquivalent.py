test_str1 = 'Panchakatla'
test_str2 = 'Pramod'

print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

res = False
for idx in range(len(test_str1)):
    if test_str1[idx:] + test_str1[:idx] == test_str2:
        res = True
        break
print("Are two strings Rotationally equal ? : " + str(res))