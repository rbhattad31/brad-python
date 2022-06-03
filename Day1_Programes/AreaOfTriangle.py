a = int(input("Enter the length of the first side"))
b = int(input("Enter the length of the second side"))
c = int(input("Enter the length of the third side"))
p = (a+b+c)
s = p/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of triangle is :",area)
print("Perimeter of triangle is :",p)
print("Semi perimeter of trianle :",s)