d = {"A":3, "B":1, "C":100}


min = min(d, key=d.get)

print(min)
