# Overflow error handling
j = 5.0
try:
    for i in range(1, 1000):
        j = j**i
        print(j)


except OverflowError as e:
    print("Overflow error happened")
    print(f"{e}, {e.__class__}")


finally:
    print('End1')


# Runtime error handling
try:
    print(emp_id)

except Exception as msg1:
    print(msg1)

finally:
    print('End2')


#  StopIteration error handling
y = [1, 2, 3]
x = iter(y)
try:
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())


except StopIteration as msg:
    print("StopIteration error handled successfully")

finally:
    print('End3')
