dict= {'key1': 500, 'key2': 200, 'key3': 300}
print("dictionary:",dict)
min_value = min(dict.values())
for key in dict:
    if dict[key]==min_value:
        print(key)