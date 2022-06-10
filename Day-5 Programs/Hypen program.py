str1=input("Enter the hypen string:")
list1=str1.split('-')
list1.sort()
str2=""
l1=len(list1)
for i in list1:
    if i==list1[l1-1]:
        str2 += i
    else:
        str2 += i + '-'
print(str2)