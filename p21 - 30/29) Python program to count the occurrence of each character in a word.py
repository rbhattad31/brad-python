string = input("Please enter your own string : ")
char = input("Please enter your own Character : ")

i = 0
count = 0

#   To ignore case sensitivity
string = string.lower()

#   Checking for match among the characters and incrementing count
while i < len(string):
    if string[i] == char:
        count = count + 1
    i = i + 1

print('The total number of times', char, 'has occurred =', count)
