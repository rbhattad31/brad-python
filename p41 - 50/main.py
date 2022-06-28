def function1():
    print("a")

    def function2():
        print("b")

        return function2

    return function1


function1()
