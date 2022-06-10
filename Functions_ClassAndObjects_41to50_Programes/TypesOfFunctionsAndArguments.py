#Default Parameter
def my_country(country):
  print("I am from " + country)
country="Indian"
my_country(country)
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
#Keyword argumnet
def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Whatsap", child3 = "Telegram")
#variable length argument
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Whtasap", "Telegram")
#mixed arguments
def bla(profile='system', *args, **kwargs):
    print ('profile', profile)
    print ('args', args)
    print ('kwargs', kwargs["testmode"])


bla(1, 2, 3, testmode=True)