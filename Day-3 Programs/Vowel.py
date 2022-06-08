print("Enter the string")
str1=input()
num_vowels=0
for char in str1:
    if char in "aeiouAEIOU":
        num_vowels = num_vowels+1
print(num_vowels)