dictionary = {'c': 100, 'b': 200, 'a': 300}

value = 200

if value in dictionary.values():
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")

for key in sorted(dictionary):
    print("%s: %s" % (key, dictionary[key]))
    