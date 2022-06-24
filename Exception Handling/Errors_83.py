# Import Error
try:
    import modulefinder
except ImportError as m:
    print("It cannot import module and submodule", m)

# Index Error
try:
    List = []
    index = 1
    element = List[index]
except IndexError as error:
    print(error)

# Key error
try:
    marks = {"sub": "Maths", "score": 72}
    print(marks["sub"])
except KeyError as a:
    print('key error', a)

# Keyboard interrupt
try:
    print('program is running')
    print('press stop')
    while True:
        pass
except KeyboardInterrupt:
    print('program interrupted')