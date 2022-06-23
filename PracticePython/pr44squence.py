def word(x):
    for i in range(len(x) + 1):
        for j in range(len(x) - 1):
            if x[j][0] > x[j + 1][0]:
                x[j], x[j + 1] = x[j + 1], x[j]

    string = ("-").join(x)
    print("Sequence After sorting :- ", string)


str = input("Enter hyphen-separated sequence of words :- ")
a = str.split("-")
word(a)

