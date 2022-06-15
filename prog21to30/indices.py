test_list = ["hyderabad", "is the", "best city", "to live in"]

# initializing K
K = "live"

print("The original list : " + str(test_list))

# using loop to iterate through list
res = []
for idx, ele in enumerate(test_list):
    if K in ele:
        res.append(idx)

# printing result
print("The indices list : " + str(res))

