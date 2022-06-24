import re
ip = "234.08.094.0196"
result = re.sub("\.0*", '.', ip)
print(result)