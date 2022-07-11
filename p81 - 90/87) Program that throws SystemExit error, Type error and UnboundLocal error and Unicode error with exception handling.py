# SystemExit error exception handling
limit = 17

if limit < 18:

    try:
        raise SystemExit

    except SystemExit:
        print("Specifying SystemError exception in this block works.")

    finally:
        print("End1")


# Type error handling
try:
    string = "Hello"
    num = 4
    print(string + num + string)


except TypeError as msg2:
    print(msg2)


finally:
    print('End2')


# UnboundLocal error handling
try:
    k = 56

    def x_try():
        print(k)
        k = 90

    x_try()


except UnboundLocalError as msg3:
    print(msg3)


finally:
    print('End3')


# Unicode error handling
try:
    a = u'dfsf\xac\u1234'
    print("The value of the above unicode literal is as follows:")
    print(ord(a[-1]))


except UnicodeError as msg4:
    print(msg4)


finally:
    print('End4')
