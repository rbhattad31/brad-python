
is_vowel=input("Enter the string:")
vowels=0

for char in is_vowel:
    if char in "aeiouAEIOU":
        vowels = vowels+1
print(vowels)