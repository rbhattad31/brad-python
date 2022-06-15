str= "ABCDEFGHIJ"
# Outer loop
for i in range(0,10):
    # inner loop
    for j in range(0,i+1):
        print(str[j],end="")
    print()