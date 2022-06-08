# appending new value to the list

L1 = ['Sai', 'Bradsol', 1997, 8096555308]
L1.append("Chillam cherla")
print(L1)

# insert value at specific position
L2 = ['Sai', 'Bradsol', 1997, 8096555308]
L2.insert(1, "Goud")
print(L2)

# add L1 content to L2 List using extend

L1.extend(L2)

print(L1)
# count the elements in the list
L3 = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 5, 5,1922, 1922]
print(L3.count(1922))
# sum the elements in the List
print(sum(L3))

# print the particular index element

print(L3.index(2))
# Print the lowest & highest element in the list
L4=[18,19,22,10,2,68,89,9,45]
print(min(L4))

print(max(L4))
# sorting the list
L4.sort(reverse=True)

print(L4)

print(L4.pop(2))

# deleting element from List

L5=["Sai","Arya","Danerys","25","23","27"]
del L5[1]
print(L5)

make=list()
make.append("Sai")
make.append(8096555308)
make.append("Chat Bot Developer")

print(make)
