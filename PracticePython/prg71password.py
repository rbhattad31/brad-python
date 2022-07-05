import re
pwd = input('enter your password')
x= True
while x:
    if (len(pwd)<6 or len(pwd)>12):
        break
    elif re.search("[a-z]",pwd) is None:
        break
    elif re.search("[A-Z]",pwd) is None:
        break
    elif re.search("[0-9]",pwd) is None:
        break
    elif re.search("[$#@]",pwd) is None:
        break
    elif re.search("\s",pwd) :
        break
    else:
        print("valid password")
        x = False
        break
if x:
    print('not a valid password')
