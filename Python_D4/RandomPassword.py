import string
import random
import string
import random

pswrd = list(string.ascii_letters + string.digits + string.punctuation)


def generate_random_password():

    length = int(input("Enter password length: "))

    random.shuffle(pswrd)

    # ## picking random characters from the list
    password = []
    for i in range(length):
     password.append(random.choice(pswrd))


    random.shuffle(password)


    print("".join(password))



generate_random_password()