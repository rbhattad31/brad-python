class Employee:
    name = "Rahul"
    age = "28"
    __salary = 10000


print(Employee().name)
print(Employee().__salary)   # Private attribute not accessible outside of class generates error
