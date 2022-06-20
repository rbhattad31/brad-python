val = int(input("Enter the Number :"))
fac_list = list()
for i in range(1, val):
    if val % i == 0:
        fac_list.append(i)
summation = sum(fac_list)

if summation > val:
    print(val, " is an abundant number")
else:
    print(val, " is not an abundant Number")
