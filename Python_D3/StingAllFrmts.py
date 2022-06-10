str1 = "Brad contech Solutions"

print(str1)
# print string using index
print(str1[5:10])
# combining two strings
str2=" Simplifying Business"

str3 = str1+str2
print(str3)

# print string multiple times
str4 = 4 * " Sai Ananthula"

print(str4)

# capitalize the Sting

str5="bRADSOL"
s1=str5.capitalize()
print(s1)

# lower the string

str6 ="sAi aNANTHULA"
s2=str6.lower()
print(s2)

# Convert String to Upper Case
str7 = "game of thrones"
s3 = str7.upper()
print(s3)

# convert first letter of the string to Uppercase
str8 = "money Heist"
s4 = str8.title()
print(s4)

# convert string upper to lower and lower to Upper
str9 = "wHEEL OF tIME"
s5 = str9.swapcase()
print(s5)
# to count the no of words in the string
str10 = 'To promote and provide assistance to creative writers through peer review, outreach programs, writers workshops, surveys, conferences, symposiums, blogs, internet tools, and forums'
print(str10.count('e'))

print(str10.count('rea'))

print(str10.count('e', 4, 40))

print(str10.find('x'))

str11 = "Process Demotions in Workday"

print(str11.split("e"))


str12 = ':'.join(['game', 'of', 'thrones'])
print(str12)








