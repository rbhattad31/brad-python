str1 = 'geeks'
str2 = 'eksge'

print("The string 1 is : ",str1 )
print("The string 2 is : ",str2)

res = False
for i in range(len(str1)):
		if str1[i: ] + str1[ :i] == str2:
			res = True
			break
print("Result: ",res)
