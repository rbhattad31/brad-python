import copy

list1 = [1,[2,3],4]
list2 = list1
# shallow copy
list3 = list1.copy()
# deep copy
list4 = copy.deepcopy(list1)

list1.append(5)
list1[1][1] = 999

print(list1)
print(list2)
print(list3)
print(list4)