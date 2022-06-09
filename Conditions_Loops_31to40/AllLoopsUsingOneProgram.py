fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
for x in fruits:
  if x == "banana":
    break
  print(x)
for x in fruits:
  pass
i = 0
#using while loop
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  if i == 3:
    break
  i += 1
for x in fruits:
  pass

