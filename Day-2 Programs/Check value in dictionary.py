import operator
dict= {'key1': 500, 'key2': 200, 'key3': 300}
print("dictionary:",dict)
print('key1' in dict)
print('key4' in dict)
print(100 in dict.values())
sorted_dict= sorted(dict.items(), key=operator.itemgetter(1))
print(sorted_dict)