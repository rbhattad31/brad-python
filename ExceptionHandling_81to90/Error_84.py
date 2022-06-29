# memory error
import gc
import os

gc.collect()


# Name Error
class Data:
    pass


try:
    print(Data)
    Data = "Hello"
except NameError as e:
    print(e)

# Not Implemented Error
try:
    class Super(object):
        @property
        def example(self):
            raise NotImplementedError("Subclasses should implement this!")


    s = Super()
    print(s.example)
except Exception as e:
    print(e)

# OS Error
try:
    filePath = 'demo.txt'
    fileDescriptor = os.open(filePath, os.O_RDWR)
    os.close(fileDescriptor)
except OSError as e:
    print(e)
