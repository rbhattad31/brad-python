dictionary = {'c': 100, 'b': 200, 'a': 300}
x = dictionary.values()
y = min(x)
print(y)
res = [key for key in dictionary if dictionary[key] == y]
print('The key to the minimum value in the dictionary is :', res)
