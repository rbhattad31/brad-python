# Import Error
try:
    import openpyxl
except ImportError as e:
    print("It cannot import module and submodule", e)

# Index Error
try:
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    index = 10
    element = myList[index]
except IndexError as e:
    print(e)

# Key error
try:
    raspberry_pi = {"name": "Raspberry Pi 4", "price": 35.00, "RAM": "4GB"}
    print(raspberry_pi["ROM"])
except KeyError as e:
    print('key error', e)

# Keyboard interrupt
try:
    print('program is running')
    print('press stop')
    while True:
        pass
except KeyboardInterrupt:
    print('program interrupted')




