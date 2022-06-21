# Python3 code to demonstrate working of
# Check if two strings are Rotationally Equivalent
# Using loop + string slicing

# initializing strings
test_str1 = 'hello'
test_str2 = 'ohell'

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# Check if two strings are Rotationally Equivalent
# Using loop + string slicing
res = False
for idx in range(len(test_str1)):
    if test_str1[idx:] + test_str1[:idx] == test_str2:
        res = True
        break

# printing result
print("Are two strings Rotationally equal ? : " + str(res))