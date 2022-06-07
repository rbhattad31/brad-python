print("Enter the list count:")
count=int(input())
print("Enter the list elements:")
list1=[]
ans=[]
for i in range(count):
    x=int(input())
    list1.append(x)
print("Enter the min range:")
min=int(input())
print("Enter the max range:")
max=int(input())
for x in list1:
    if x>=min and x<=max:
        ans.append(x)
print("Coerced elements\n",ans)