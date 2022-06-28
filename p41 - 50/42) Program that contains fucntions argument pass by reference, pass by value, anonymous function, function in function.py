#   function argument pass by reference
#   When we pass something by reference any change we make to the variable inside the function then those changes are
#   reflected to the outside value as well


def alter_list(list_):
    list_.append([1, 2, 3, 4])
    print("Values inside the function: ", list_)
    return


my_list = [10, 20, 30]
alter_list(my_list)
print("Values outside the function: ", my_list)

#   function argument pass by value
#   When we pass something by value then the changes made to the function or copying of the variable are not reflected
#   back to the calling function


students = {'Jim': 12, 'Tim': 14, 'Tom': 10}


def test():
    student = {'Sam': 20, 'Steve': 21}
    print("Inside the function", students)
    print("Inside the function", student)
    return


test()
print("Outside the function:", students)


# Defining anonymous or lambda function


square = lambda x: x * x

# Defining anonymous or lambda function
# and passing function as an argument


cube = lambda func: func ** 3

print("\nsquare of 2 is :" + str(square(2)))
print("\nThe cube of " + str(square(2)) + " is " + str(cube(square(2))))


#   Function in function


def print_msg(msg):
    def post():
        print(msg)

    post()


print_msg("\nHello")
