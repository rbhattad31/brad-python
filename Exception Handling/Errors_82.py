# AssertionError
try:
    a = 1
    b = 0
    assert b!= 0, \
        "Invalid Operation"
    print(a / b)


except AssertionError as msg:
    print(msg)

# Attribute Error
try:
    m = 0
    m.append(3)
except Exception as message:
    print(message)

# EOF Error
name = "Shakespear"
author = "some guy"
native = " America."
print("The {} book was devised by {}. {}".format(name, author, native))

# Floating point error
val = 3.4 + 0.11
# with error
print(val)
# without error
print(f"val = {val:.2f}")


