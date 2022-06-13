Numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("The original list is:" + str(Numbers_list))

i, j = -1, 11

Y = True
for ele in Numbers_list:
    if ele < i or ele >= j:
        Y = False
        break

print("Does list contain all elements in range : " + str(Y))
