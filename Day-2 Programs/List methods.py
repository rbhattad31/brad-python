l1=[1,'a',200,300,400]
print("List Elements:\n",l1)
#Update element using index
l1[0]=100
l1[1]=150
print("List elements after update:\n",l1)
#Append
l1.append(500)
print("List elements after append:\n",l1)
#pop element
l1.pop()
print("List elements after pop:\n",l1)
#reverse list
l1.reverse()
print("List elements after reverse:\n",l1)
#insert list
l1.insert(1,250)
print("List elements after insert:\n",l1)
#sort list
l1.sort()
print("List elements after sorting:\n",l1)
#concatenating list
l2=[1000,2000]
l1=l1+l2
print("List elements after concatenating:\n",l1)
