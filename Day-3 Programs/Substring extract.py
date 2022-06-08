str1 = ["Gfg is good", "for Geeks", "I love Gfg", "Its useful"]
K = "Gfg"
ans=[]
print("The original list : " + str(str1))
for val in range(len(str1)):
    if K in str1[val]:
        ans.append(val)
print("The indices list : ",ans)