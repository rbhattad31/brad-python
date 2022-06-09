a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

 # nested if
if a > 10:
  print("Above ten,")
  if a > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#Short Hand if
if a > b: print("a is greater than b")
#Short Hand if...Else
print("A") if a > b else print("B")
#Ternary Operator
print("A") if a > b else print("=") if a == b else print("B")