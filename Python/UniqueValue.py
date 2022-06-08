
list1 = [1, 2, 2, 5, 8, 4, 4, 8]
l1 = []

count = 0


for item in list1:
	if item not in l1:
		count += 1
		l1.append(item)


print("No of unique items are:", count)
