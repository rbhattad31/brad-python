# Python 3 code for triangular
# patterns of alphabets
n = 5
if __name__ == '__main__':

    n = 5;
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(ord('A') + j - 1),
                  end=" ");

        print("");

# This code is contributed by 29AjayKumar