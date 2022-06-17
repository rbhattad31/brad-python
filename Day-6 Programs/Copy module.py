import copy
l1 = [5, 6, 7, 8, [10, 2]]
#shallow copy
l2 = copy.copy(l1)
print("shallowcopy")
print("List before change:", l1)
#change elements in list
l2[0] = 100
print("List after change:", l1)
#change in nested
l2[4][0]=100
print("List after nested:", l1)

#Deep copy
print("Deepcopy")
l2 = copy.deepcopy(l1)
print("List before change:", l1)
#change elements in list
l2[0] = 200
print("List after change:", l1)
#change in nested
l2[4][0]=200
print("List after nested:", l1)



