from itertools import permutations
count=3
print("Enter the 3 list elements:")
list1=[]
ans=[]
for i in range(count):
    x=int(input())
    list1.append(x)
combination = permutations(list1, 3)
print("combinations")
for i in combination:
    print(i)