str = input("Enter your String")


out = {x: str.count(x) for x in set(str)}


print("Occurrence of all characters in " + str +" is",out)