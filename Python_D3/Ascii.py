str=input("Enter your string")
ascii_codes=[]


for i in range(len(str)):
    ascii_codes.append(ord(str[i]))


print('The ASCII value of each character are:',ascii_codes)