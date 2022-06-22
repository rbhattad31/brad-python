def formula_1(a, b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    finally:
        print("code executed")


formula_1(2.0, 3.0)
formula_1(3.0, 3.0)
