test_dict = {'Ram': 30, 'Teja': 29, 'Nikhil': 31, 'Jagan': 43, 'Madhu': 32, 'Raj': 38}

temp = min(test_dict.values())
result = [key for key in test_dict if test_dict[key] == temp]
print(result)
