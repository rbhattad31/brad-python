# default arguments
def greet(arg_1="Hi", arg_2="Ram"):
    print(arg_1 + " " + arg_2)

greeting = input("Enter first input: ")
name = input("Enter second input: ")
greet()

# Keyword Arguments
def greet(arg_1, arg_2):
  print(arg_1 + " " + arg_2)

greeting1 = input("Enter first input: ")
name1 = input("Enter second input: ")
greet(arg_1=greeting,arg_2=name)

# variable length argument
def sum(*nos):
    total = 0
    for i in nos:
        total = total + i
    print(total)


sum()
sum(-3, 4, 5)
sum(1, 2, 3, 4, 5)

# mixed argument
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" % result)