# Write a program that includes all types of loops - for, while, do while, pass, break and continue

print("\nString Iteration")
s = 'World'
for i in s:
    print(i)

count = 0
while count < 3:
    count = count+1
    print("Hello World")

#   Do while loop with while, if conditions
i = 1
while True:
    print(i)
    i = i + 1
    if i > 5:
        break

a = 33
b = 200

if b > a:
    pass

i = 0
while i < 9:
    i += 1
    if i == 3:
        continue
print(i)
