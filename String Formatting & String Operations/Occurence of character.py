inp_str = input("Enter input:")

result = {}

for ele in inp_str:
    if ele in result:
        result[ele] += 1
    else:
        result[ele] = 1

print("Occurrence of all characters in input is :\n " + str(result))