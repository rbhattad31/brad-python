# Opening the file in reading mode


with open(r"check_file.txt", 'r') as fp:
    x = len(fp.readlines())
    print('Total lines:', x)


# Function to check for string in a file


def check_if_string_in_file(file_name, string_to_search):

    with open(file_name, 'r') as read_obj:

        for line in read_obj:

            if string_to_search in line:
                return True
    return False


# Checking for "is" in the file


if check_if_string_in_file('check_file.txt', 'is'):
    print('Yes, string found in file')
else:
    print('String not found in the file')
