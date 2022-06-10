str1 = input("Enter your first String")
str2 = input("Enter your Second String")


print("The original string 1 is : " + str(str1))
print("The original string 2 is : " + str(str2))


res = False
for idx in range(len(str1)):
    if str1[idx:] + str1[:idx] == str2:
        res = True
        break


print("Are two strings Rotationally equal ? : " + str(res))