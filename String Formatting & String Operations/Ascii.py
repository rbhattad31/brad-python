Asc_Char = input("Enter your String : ")

Asc_Char_length = len(Asc_Char)

for i in range(Asc_Char_length):
    print("The ASCII Value of Character %c = %d" % (Asc_Char[i], ord(Asc_Char[i])))