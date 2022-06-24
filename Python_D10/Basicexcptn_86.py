# SyntaxError
while True print('Hello world'):

# IndentationError
try:
 x = 5
 y = 9
 z=x+y


except IndentationError :
print("maintain exception")

# Tab Error

numbers = [3.50, 4.90, 6.60, 3.40]
def calculate_total(purchases):
    total = sum(numbers)
        return total
total_numbers = calculate_total(numbers)
print(total_numbers)
