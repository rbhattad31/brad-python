# Import Error
try:
    import openpyxl
except ImportError as e:
    print("It cannot import module and submodule", e)
# Index Error
array = [0, 1, 2]
print(array[3])

# Key Error
array = {'a': 1, 'b': 2}
print(array['c'])
# KeyboardInterrupt
try:
    print('program is running')
    print('press stop')
    while True:
        pass
except KeyboardInterrupt:
    print('program interrupted')
