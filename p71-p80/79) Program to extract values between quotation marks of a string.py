import re
input_string = ' strings  "Hello" "World" '

print(re.findall('"([^"]*)"', input_string))
