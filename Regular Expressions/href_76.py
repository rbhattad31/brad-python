import re


def get_href_links(text):
    regex = r'href=[\'"]?([^\'" >]+)'
    match = re.findall(regex, text)
    return match


with open('sourceFile.txt') as file:
    data = file.read()

print(get_href_links(data))