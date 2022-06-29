def is_abundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctr_sum > n
a = int(input("Enter the number?"))
if is_abundant(a):
    print("The number is Abundant.")
else:
    print("The number is not Abundant.")