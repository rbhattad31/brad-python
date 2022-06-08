bag={'money': 200, 'Tissues': 75, 'phones': 3}

print(bag.get('money'))

print(bag.keys())

print(bag.values())

print(bag.items())

bag.clear()

print(bag)

Bank={'system':20,"currency":200000,"employees":35,"punes":4,"name":"State Bank of India"}

Copy=Bank.copy()

print(Copy)

Defvalue = Bank.setdefault("name")
print("Third_value:", Defvalue)

Dict1 = {'A': 'Bradsol', 'B': 'Contech', }
Dict2 = {'B': 'IT Solutions'}


print(Dict1)


Dict1.update(Dict2)


print(Dict1)