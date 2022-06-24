import re
import itertools

text = input("Enter your card number")
print(len(text) < 16)

l = [(k, sum(1 for i in g)) for k, g in itertools.groupby(text)]

if re.search(r'^[456]+', text) and len(text) == 16 and re.search(r'[\d]', text) and all(v <= 3 for k, v in l) and bool(
        re.search(r'\s', text)) is False and bool(re.search(r'[a-z]', text)) is False or (
        bool(re.search(r'-', text)) is True and len(text) == 19):
    print("it passed")

else:
    print("Invalid card details")
