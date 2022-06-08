def myComb(L):
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter third number:"))

    L.append(a)
    L.append(b)
    L.append(c)
    for p in range(3):
        for q in range(3):
            for r in range(3):

                # check if the indexes are not
                # same  
                if (p != q and q != r and p != r or p == q, p == r, q == r):
                    print(L[p], L[q], L[r])


myComb([])