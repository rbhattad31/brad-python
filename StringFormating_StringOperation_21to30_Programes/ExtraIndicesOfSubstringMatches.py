test_list = ["Pmd is good", "for Pramod", "I love Pmd", "Its useful"]
P = "Pmd"
print("The original list : " + str(test_list))
res = []
for idx, ele in enumerate(test_list):
    if P in ele:
        res.append(idx)
print("The indices list : " + str(res))