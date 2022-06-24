
# Example-1
class DemoException(Exception):
    def __init__(self, message_1):
        super().__init__(message_1)


message = "Exception Triggered! Something went wrong."


def trigger_exception(num_1):
    if num_1 == 0:
        raise DemoException(message)
    else:
        print(num_1)


try:
    trigger_exception(0)
    print("Code has successfully been executed.")
except DemoException:
    print("Error: Number should not be 0.")

# Example -2


class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


class ValueTooLargeError(Error):
    pass


number = 10
try:
    i_num = int(input("Enter a number: "))
    if i_num < number:
        raise ValueTooSmallError
    elif i_num > number:
        raise ValueTooLargeError
except ValueTooSmallError:
    print("This value is too small, try again!")
    print()
except ValueTooLargeError:
    print("This value is too large, try again!")
    print()