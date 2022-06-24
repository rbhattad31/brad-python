import re

def remove_duplicates(text):
    regex = r'\b(\w+)(?:\W+\1\b)+'
    return re.sub(regex, r'\1', text, flags=re.IGNORECASE)

with open('welcome.txt') as file:
    data = file.read()

print(remove_duplicates(data))


