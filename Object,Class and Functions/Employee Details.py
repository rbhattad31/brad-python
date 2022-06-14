class Employee:
    name = " "
    age = 0
    salary = 0

    def __init__(self, name, age, sal):
        self.name=name
        self.age = age
        self.salary=sal

details=Employee("Ram", 34, 24400)
print(details.name)
print(details.age)
print(details.salary)