num0 = 10

try:
    num1 = input("Enter 1st number:")
    num2 = input("Enter 2nd number:")
    result = (int(num1) * int(num2))/(num0 * int(num2))

except ValueError as msg1:
    print(msg1)
    exit()

except ZeroDivisionError as msg2:
    print(msg2)
    exit()

finally:
    print('End')
