# Python3 code to demonstrate
# removing duplicate substrings
# using set() + split()

# initializing list
test_list = ['aa-aa-bb', 'bb-cc', 'gg-ff-gg', 'hh-hh']

# printing original list
print("The original list : " + str(test_list))

# using set() + split()
# removing duplicate substrings
res = [set(sub.split('-')) for sub in test_list]

# print result
print("The list after duplicate removal : " + str(res))