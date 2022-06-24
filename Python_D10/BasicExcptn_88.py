# UnicodeEncodeError
u = 'é'
print("Integer value for é: ", ord(u))
print("Converting the encoded value of é to Integer Equivalent: ", chr(233))
print("UNICODE Representation of é: ", u.encode('utf-8'))
print("ASCII Representation of é: ", u.encode('ascii'))

# UnicodeDecodeError
str(b'\xff', 'utf8')

# Value Error

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


# ZeroDivisionError
def this_fails():
    y = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
