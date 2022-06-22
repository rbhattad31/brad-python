import re

pattern = r"^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$"


def check_valid_card(no):
    if re.match(pattern, no):
        print("card is valid")
    else:
        print("card is not valid")


card_no = input("enter the card number: ")
check_valid_card(card_no)

