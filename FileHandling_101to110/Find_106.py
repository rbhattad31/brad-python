import os


def counter():
    # variable to store total word count
    num_words = 0

    # variable to store total line count
    num_lines = 0

    # variable to store total character count
    num_charc = 0

    # variable to store total space count
    num_spaces = 0

    with open('count.txt', 'r') as f:
        for line in f:
            line = line.strip(os.linesep)

            wordslist = line.split()

            num_lines = num_lines + 1

            num_words = num_words + len(wordslist)

            num_charc = num_charc + sum(1 for c in line
                                        if c not in (os.linesep, ' '))

            num_spaces = num_spaces + sum(1 for s in line
                                          if s in (os.linesep, ' '))

    # printing total word count
    print("Number of words in text file: ", num_words)

    # printing total line count
    print("Number of lines in text file: ", num_lines)

    # printing total character count
    print("Number of characters in text file: ", num_charc)

    # printing total space count
    print("Number of spaces in text file: ", num_spaces)


if __name__ == '__main__':
    fname = 'count.txt'
    try:
        counter()
    except:
        print('File not found')
