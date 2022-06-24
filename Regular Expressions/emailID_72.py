import re

def solve(m):
   pattern = "[A-Za-z0-9-_]+@[A-Za-z0-9]+\.[a-z]{1,3}$"
   if re.match(pattern, m):
      return True
   return False

s = input("Enter your mail Id: ")
print(solve(s))