test_list = ["welcome", "To", "welcome Back", "welcome To New World"]


# using loop to iterate for each string
test_list.sort(key=len)
res = []
for i, value in enumerate(test_list):

    # concatenating all next values and checking for existence
    if value not in ', '.join(test_list[i+ 1:]):
        res.append(value)

# printing result
print("The reduntant list : " + str(res))
