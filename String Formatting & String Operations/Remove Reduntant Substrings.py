List = [1, 3, 4, 1, 2, 2, 5, 2, 1, 7, 0, 9]

Empty_list = []

for i in List:
    if i not in Empty_list:
        Empty_list.append(i)

print(Empty_list)
