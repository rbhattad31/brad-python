import copy

l1 = [2, 4, 5, 78, 90]
dc = copy.deepcopy(l1)
print(dc)
dc[0] = 1922

print(dc)
print("after deep copy", l1)
# shallow copy

l2 = [5, 9, 87, 9]
sc = copy.copy(l2)
print(l2)

sc[2] = 1922
print(sc)

print("after shallow copy", sc)
