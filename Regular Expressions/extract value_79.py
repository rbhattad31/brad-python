import re
text1 = ' "RPA", "Automation", "A360",'
print(re.findall(r'"(.*?)"', text1))