#Default Parameter
def my_country(country):
  print("I am from " + country)
country="Sweden"
my_country(country)
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
#Keyword argumnet
def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#variable length argument
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#mixed arguments
def bla(profile='system', *args, **kwargs):
    print ('profile', profile)
    print ('args', args)
    print ('kwargs', kwargs["testmode"])


bla(1, 2, 3, testmode=True)