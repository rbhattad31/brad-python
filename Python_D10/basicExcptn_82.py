# assertion error
try:
    u_input = int(input("Enter the  Number"))
    assert u_input % 2 == 0
    print(u_input, " is an even number")
except AssertionError:
    print(u_input, " is an odd number")

# Attribute error

greeting = "Hi,my name is {}".format("Sai")
print(greeting)

# EOF error
try:
    n = int(input())
    print(n * 10)

except EOFError as e:
    print(e)
