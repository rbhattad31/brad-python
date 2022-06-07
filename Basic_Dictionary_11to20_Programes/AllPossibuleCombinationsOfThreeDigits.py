firstDigit = 1
secondDigit = 9
thirdDigit = 2
digitsList = []
digitsList.append(firstDigit)
digitsList.append(secondDigit)
digitsList.append(thirdDigit)
for i in range(3):
    for j in range(3):
        for k in range(3):
            if(i != j & j != k & k != i):
                print(digitsList[i], digitsList[j], digitsList[k])