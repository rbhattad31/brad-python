input_list = [1, 2, 2, 5, 8, 4, 4, 8,9]

List = []
count = 0

for item in input_list:
    if item not in List:
        count += 1
        List.append(item)

print("No of unique items are:", count)
