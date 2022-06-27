import copy

# deepcopy
P = [[1, 2, 3], [4, 5, 6]]
cp = copy.deepcopy(P)
cp[0][1] = 97
print("deep copy :", cp)

# shallow copy
V = copy.copy(P)
V[0][2] = 79
print("shallow copy :", V)

# change in nested
P[1][1] = 100
print("List after nested:", P)



