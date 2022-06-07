test_dict = {'Gfg' : 11, 'for' : 2, 'CS' : 11, 'geeks':8, 'nerd':2}
print("The original dictionary is : " + str(test_dict))
temp = min(test_dict.values())
res = [key for key in test_dict if test_dict[key] == temp]
print("Keys with minimum values are : " + str(res))