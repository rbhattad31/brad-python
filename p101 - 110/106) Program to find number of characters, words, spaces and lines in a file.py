file = open("file3.txt", "r")

count = 0
while True:

    # This will read each character
    # and store in char
    char = file.read(1)

# Counting number of spaces
    if char == " ":
        count += 1
    if not char:
        break

number_of_lines = 0
number_of_words = 0
number_of_characters = 0

for line in file:
    lines = line.strip("\n")
    words = lines.split()
    number_of_lines += 1
    number_of_words += len(words)
    number_of_characters += len(lines)

file.close()

print("No of lines are :", number_of_lines, " No of words are :", number_of_words,
      " No of characters are :", number_of_characters)

print("No of spaces are : ", count)
