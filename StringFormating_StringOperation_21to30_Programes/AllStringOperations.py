string = "Hello world I am from \"India\""
str1 = 'Pramod'
str2 = 'Python'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)
#Comparison '==' Operator
print(str1 == str2)
# != Operator
print(str1 != str2)
print('P' in 'Pramod')
#[] string slicing operatore
print(str1[1])
print(str2[-2])
print(str1[1:5])
print(str2[1:-3])
print(str1[2:])
print(str2[:5])
print(str1[:-2])
print(str1[-2:])
print(str2[::-1])
#Escape Sequence Operator “\”
print(string)
#String Formatting Operator “%”
name = "india"
age = 19
marks = 20.56
string1 = 'Hey %s' % (name)
print(string1)
string2 = 'my age is %d' % (age)
print(string2)
string3= 'Hey %s, my age is %d' % (name, age)
print(string3)
string3= 'Hey %s, my subject mark is %f' % (name, marks)
print(string3)