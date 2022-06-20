def check_armstrong(x):
    result = 0
    n = 0
    temp = x

    while temp != 0:
        temp = temp//10
        n = n + 1

    temp = x

    # Check if the number is armstrong
    while temp != 0:
        reminder = temp % 10
        result = result+pow(reminder, n)
        temp = temp//10

    if result == x:
        print(x, "is an armstrong number.")
    else:
        print(x, "is not an armstrong number.")


n = int(input("Enter the number to check armstrong: "))

check_armstrong(n)
