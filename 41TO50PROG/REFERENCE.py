student = {'jeev': 12, 'Anil': 14, 'Priya': 10}
def test(student):
    new = {'Sun': 20, 'Suma': 21}
    student.update(new)
    print("Inside the function", student)
    return
test(student)
print("Outside the function:", student)
