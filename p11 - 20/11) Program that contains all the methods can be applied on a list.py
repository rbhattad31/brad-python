Numbers = [1, 2, 3, 4, 5]

print(Numbers)  # 0

print(Numbers[0])    # 1

Numbers.append(6)
print(Numbers)   # 2

x = Numbers.copy()
print(x)    # 3

y = Numbers.count(3)
print(y)    # 4

alphabets = ['a', 'b', 'c']
Numbers.extend(alphabets)

print(Numbers)   # 5

x = Numbers.index('b')
print(x)    # 6

Numbers.insert(1, "orange")
print(Numbers)   # 7

j = Numbers.pop(1)
print(j)    # 8

Numbers.remove(6)
print(Numbers)   # 9

Numbers.reverse()
print(Numbers)   # 10

alphabets = ['c', 'b', 'a']
alphabets.sort()

print(alphabets)    # 11

Numbers.clear()
print(Numbers)  # 12
