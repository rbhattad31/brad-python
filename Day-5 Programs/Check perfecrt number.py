num = int(input("Enter any number: "))
sum_1 = 0
for i in range(1, num):
    if(num % i == 0):
        sum_1 = sum_1 + i
if (sum_1 == num):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")