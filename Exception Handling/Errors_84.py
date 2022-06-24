# Memory Error

import gc
import os

gc.collect()

# Name Error
try:
    print(data)
    data = "Hello"

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
except Exception as error:
    print(error)

# OS Error
try:
    filePath = 'demo.txt'
    fileDescriptor = os.open(filePath, os.O_RDWR)
    os.close(fileDescriptor)
except OSError as e:
    print(e)