print("Enter a String: ", end="")
string = input()
for char in string:
    ascii_value = ord(char)
    print(char, "\t", ascii_value)
