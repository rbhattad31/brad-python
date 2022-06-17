import sys

# system version
print(sys.version)

# stderr
sys.stderr.write("This is stderr text\n")
# stdout
sys.stdout.write("This is stdout text\n")
# pass input from terminal
if len(sys.argv) > 1:
    print("\nName of Python script:", sys.argv[0])
    print("\nAddition result")
    print(float(sys.argv[1])+float(sys.argv[1]))




