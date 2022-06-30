print("Enter sample_1 as file name")
print("Enter the Name of File: ")
fileName = str(input())
fileHandle = open(fileName+'.txt', "a")
print("Enter the Text to Append in Given File: ")
print("Enter new line without text to exit")
while True:
    text = str(input())
    if len(text) > 0:
        fileHandle.write("\n")
        fileHandle.write(text)
    else:
        break
fileHandle.close()