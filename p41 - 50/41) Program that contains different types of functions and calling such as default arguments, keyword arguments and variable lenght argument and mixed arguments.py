# function using default arguments


def vehicles(vehicle):
    print("The " + vehicle, "is a luxury vehicle")


vehicles("Car")

# function using keyword arguments


def vehicles(vehicle1, vehicle2, vehicle3):
    print("The cheapest vehicle is " + vehicle1)
    print("The second cheapest vehicle is " + vehicle2)
    print("The third cheapest vehicle is " + vehicle3)


vehicles(vehicle1="cycle", vehicle2="auto", vehicle3="car")


# function using variable length argument and mixed arguments


def multiply(*args):
    y = 1
    for num in args:
        print(num)
        y *= num
    print(y)


multiply(3, 7)
multiply(9, 8)
multiply(3, 4, 7)
multiply(5, 6, 10, 8)
