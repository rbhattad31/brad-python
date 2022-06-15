def check_rotations(first_string, second_string):
    size1 = len(first_string)
    size2 = len(second_string)

    if size1 != size2:
        return 0

    new_string = first_string + second_string
    print(new_string)

    if new_string.count(second_string) > 0:
        return 1
    else:
        return 0


first_string = input("Enter first string:")
second_string = input("Enter second string:")

if check_rotations(first_string, second_string):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")
