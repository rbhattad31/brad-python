# syntax error[run code separately]
try:
    eval('x === x')
except SyntaxError as e:
    print(e)

# System error
# [Cause when internal system error occurs]

# Tab error & Indentation error
try:
    numbers = [3.50, 4.90, 6.60, 3.40]
    def calculate_total(purchases):
        total = sum(numbers)
            return total
    total_numbers = calculate_total(numbers)
    print(total_numbers)
except TabError as e:
    print(e)