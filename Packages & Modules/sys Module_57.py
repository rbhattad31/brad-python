import sys
# path where the python modules are searched
print(sys.path)
# it shows current version
print(sys.version)
# command line arguments can pass
print(sys.argv)
# it identifies the host os
print(sys.platform)
# it specifies the path of python executable file
print(sys.executable)
# returns list of available modules
print(sys.modules)
# it shows python copyright info
print(sys.copyright)

# return output value
print(sys.stdout.write('Hello World \n'))
# return output as error value in red color
print(sys.stderr.write('Hello World \n'))
# return size in bytes
print(sys.getsizeof(134))
print(sys.getsizeof(14.8))

# exit() function stops the program
print("Hi")
sys.exit()
print("Hello")
