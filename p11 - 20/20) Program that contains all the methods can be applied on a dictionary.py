Car = {'Brand': 'BMW',
       'Model': 'Sedans',
       'Year': 2018
       }

a = Car.copy()
print(a)

b = Car.get('Model')
print(b)

c = Car.items()
print(c)

d = Car.keys()
print(d)

Car.pop("Model")
print(Car)

e = Car.setdefault('Model', 'SUV')
print(Car)

Car.popitem()
print(Car)

Car.update({'color': 'White'})
print(Car)

f = Car.values()
print(f)

Car.clear()
print(Car)

j = ('key1', 'key2', 'key3')
k = 'BMW'
dictionary = dict.fromkeys(j, k)
print(dictionary)
