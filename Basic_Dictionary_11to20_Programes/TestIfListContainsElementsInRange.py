test_list = [4, 5, 6, 7, 3, 9]

print("The original list is : " + str(test_list))
i, j = 3, 10
res = all(ele >= i and ele < j for ele in test_list)
print("Does list contain all elements in range : " + str(res))