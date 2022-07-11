# Syntax Error exception handling

try:
    print(eval('Hello World'))

except SyntaxError as err:
    print('Syntax error %s (%s-%s): %s', err.filename, err.lineno, err.offset, err.text)
    print(err)

finally:
    print("End1")


# Indentation Error exception handling

try:
    numbers = "12345678"
    num = numbers[7]

except IndentationError as msg2:
    print(msg2)

finally:
    print("End2")


# Tab Error exception handling

try:
    numbers = [3.50, 4.90, 6.60, 3.40]


    def calculate_total(purchases):
        total = sum(numbers)
        return total

    total_numbers = calculate_total(numbers)
    print(total_numbers)

except TabError as msg3:
    print(msg3)

finally:
    print("End3")


# System Error exception handling

try:
    x = input()
    print('Try using KeyboardInterrupt')

except KeyboardInterrupt:
    print('Caught Internal error')  # Interrupt the execution

else:
    print('No exceptions are caught')

finally:
    print('End4')
