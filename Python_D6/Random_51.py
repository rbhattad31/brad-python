import random

value = random.randint(1,5)
print(value)

value2 =random.uniform(1,10)
print(value2)

greet =["Hi", "Hello", "Hola", "Hey"]

value3 = random.choice(greet)
print(value3 + " Sai")

deck =list(range(1,53))
random.shuffle(deck)
hand = random.sample(deck,k=5)
print(deck)
print(hand)
