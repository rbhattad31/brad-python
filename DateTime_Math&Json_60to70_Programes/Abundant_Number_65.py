input_no = int(input("Enter a number : "))
total = 0

is_abundant = 0

for i in range(1, input_no):

    if input_no % i == 0:

        total = total + i
        if total > input_no:
            is_abundant = 1
            break

if (total > input_no) or (is_abundant == 1):
    print("It is an abundant number.")
else:
    print("It is not an abundant number.")
