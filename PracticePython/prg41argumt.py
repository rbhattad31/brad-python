def demo(name, age = "30"):
   """
   This function displays the
   name and age of a person

   If age is not provided,
   it's default value 30 would
   be displayed.
   """

   print(name + " is " + age + " years old")

demo("Steve")
demo("Lucy", "20")
demo("Bucky", "40")