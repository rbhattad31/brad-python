def rec_sum(n):
    if n <= 1:
        return n
    else:
        return n + rec_sum(n - 1)


num = int(input('enter a number: '))
if num < 0:
    print("Enter a number")
else:
    print("The sum is", rec_sum(num))
