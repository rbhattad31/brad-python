class Employee:
    count = 0

    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary


emp1 = Employee("kate", "mgr", 10000)
print(emp1.name)
print(emp1.designation)
print(emp1.salary)