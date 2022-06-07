pramod = [1,1,2.2,'pramod','True']
print(pramod)

pramod.append(2)
print(pramod)

pramod.extend([9,9,7,7])
print(pramod)

pramod.insert(1,'python')
print(pramod)

print(pramod.count(1))

print(len(pramod))

pramod.pop(0)
print(pramod)

pramod.reverse()
print(pramod)

for i in pramod:
    print(i)
