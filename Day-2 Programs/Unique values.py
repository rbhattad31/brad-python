print("Enter the list count:")
count=int(input())
print("Enter the list elements:")
list1=[]
ans=[]
for i in range(count):
    x=int(input())
    list1.append(x)
for i in list1:
    if i not in ans:
        ans.append(i)
print("unique elements:\n",ans)

