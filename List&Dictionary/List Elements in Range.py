test_List = [4,7,9,2,6]

a,b = 3,10

result = True
for element in test_List:
    if element < a or element >= b:
        result = False
        break
print(result)

