print("Enter the list count:")
count=int(input())
print("Enter the list elements:")
list1=[]
ans=[]
for i in range(count):
    x=int(input())
    list1.append(x)
for x in list1:
    if x%2==0:
        ans.append(x)
print("Even numbers:\n",ans)