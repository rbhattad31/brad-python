# pass by reference
def greet():
    print("Hello")

name = input("Enter the Input: ")
greet()
print(name)

# pass by value
def greet(word):
    msg = "Hello " + word
    print(msg)

name = input("Enter the Input: ")
greet(word=name)

# Anonymous (lambda) functions
def with_lambda(x):
    return x(10)
print(with_lambda(lambda x: x*x))

# Function in Function
def outer_func():

    def inner_func():

        print("Hello, World!")
    inner_func()

outer_func()
