print('Enter the string :')
String = input()
a = 0
e = 0
i = 0
o = 0
u = 0

for char in String:

    if 'a' in char:
        a = a + 1

    elif 'e' in char:
        e = e + 1

    elif 'i' in char:
        i = i + 1

    elif 'o' in char:
        o = o + 1

    elif 'u' in char:
        u = u + 1

    else:

        print("No vowels found")
        break

print("The frequency of the vowel a in the string is ", a)

print("The frequency of the vowel e in the string is ", e)

print("The frequency of the vowel i in the string is ", i)

print("The frequency of the vowel o in the string is ", o)

print("The frequency of the vowel u in the string is ", u)
