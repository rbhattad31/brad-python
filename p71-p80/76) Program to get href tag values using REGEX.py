# take a text file that contains source code of a webpage - and write a program to read the file and get all the 'href'
# html tag values using Regex and write into a new text file or console


import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://docs.python.org"
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(https?://.*?)"', html)
for link in links:
    print(link.decode())
    with open('source code.txt') as f:
        contents = f.readlines()
