class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def empname(self):
        return self.name
    def empage(self):
        return self.age
    def __empsalary__(self):
        return self.salary

emp1 = Employee('Sai',25,35000)

# emp1.__empsalary__()
# Employee.__empsalary__(emp1)

emp1.empage()
Employee.empage(emp1)
