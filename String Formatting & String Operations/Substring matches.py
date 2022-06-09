string = ["Welcome", "To", "Bradsol", "World"]
value = "o"
result=[]
for char in range(len(string)):
    if value in string[char]:
        result.append(char)
print("The indices list : ",result)