try:
    eval('x === x')
except SyntaxError as e:
    print(e)


try:
    numbers = [3.5, 14.90, 6.76, 13.4]
    def calculate_total():
        total = sum(numbers)
        return total
    total_numbers = calculate_total()
    print(total_numbers)
except TabError as e:
    print(e)