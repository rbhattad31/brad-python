dic = {'name': 'pramod','age': 24,'phoneno': 9948506766}
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.copy())


print(dic['name'])

dic.pop('name')
print(dic)
print(dic.popitem())

dic.update({'adders':'hyderabad'})
print(dic)

dic.clear()
print(dic)

