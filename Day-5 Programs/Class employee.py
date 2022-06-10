class Employee:
        count=0
        def __init__(self, name, desig, salary):
            self.name=name
            self.desig=desig
            self.__salary=salary

e1=Employee("John", "Manager", 80000)
print(e1.name)
print(e1.desig)
print(e1.__salary)
