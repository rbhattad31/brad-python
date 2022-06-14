
ui = int(input("Enter your age"))
if ui > 18:
    print("You can Vote")
else:
    print("Your age is less than 18,you can't vote")


balance = int(input("Enter your account balance"))

if balance == 1000:
    print("Your account type is Savings")

elif balance < 1000:
    print("Your account is currently on Hold")
else:
    print("Your account type is checking")

# Nested if
x = 41

if x > 10:
 print("Above ten,")
if x > 20:
 print("and also above 20!")
else:
 print("but not above 20.")


# Short Hand if else

a = int(input('Enter your age'))
b = int(input('Enter your friend  age'))
print("you are elder than your friend") if a > b else print("you are younger to your friend")

# Short Hand if

if a > b: print(" your friend is older than you")

# pass

a = 33
b = 200

if b > a:
 pass