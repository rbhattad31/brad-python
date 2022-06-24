import re
flag = 0
phone_num = int(input())
while True:
    if phone_num > 10 or phone_num < 10 :
        flag = -1
        break
    elif not re.findall("\d",str(phone_num)):
       flag = -1
       break
    else:
        flag = 0
        print("phone number is valid")
        break
if flag == -1:
    print("phone number is not valid")

