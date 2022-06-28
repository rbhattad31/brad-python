inputstring = 'some strings are present in between "Pramod" "Learning" "RPA" '


result = inputstring.split('"')[1::2]
print(result)

