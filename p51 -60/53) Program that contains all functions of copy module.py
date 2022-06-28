import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 64
new_list[0][2] = 20

#   change in old list is reflected in new list in shallow copy
print("Old list:", old_list)
print("New list:", new_list)


old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][1] = 64
new_list[0][2] = 20

#   change in old list is not reflected in new list in deep copy
print("Old list:", old_list)
print("New list:", new_list)
