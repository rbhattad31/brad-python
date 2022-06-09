str1 = 'geeks'
str2 = 'eksge'

result = False
for i in range(len(str1)):
		if str1[i: ] + str1[ :i] == str2:
			result = True
			break
print(result)