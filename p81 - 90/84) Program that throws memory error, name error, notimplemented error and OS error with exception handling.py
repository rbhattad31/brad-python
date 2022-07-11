import os
import numpy as np

# Memory error handling
try:
    np.random.uniform(low=1, high=10, size=(10000000000000000000000, 10000000000000000000000000000000000000))

except Exception as error:
    print(error)

finally:
    print("End1")


# Name error handling
def name_error_message():

    try:
        x = "Excel"
        print(x)
        print(xy)
        return y

    except NameError as msg1:
        return msg1

    finally:
        print("End2")


print(name_error_message())


# NotImplemented error handling
try:
    class Super(object):
        @property
        def example(self):
            raise NotImplementedError("Subclasses should implement this!")
    s = Super()
    print(s.example)
except Exception as e:
    print(e)


finally:
    print('End3')


# OS error handling
r, w = os.pipe()

try:
    print(os.ttyname(r))

except Exception as error:
    print(error)

finally:
    print('End4')
