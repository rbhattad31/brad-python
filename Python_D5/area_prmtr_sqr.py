# Method 1
#
#     side = int (input ("Enter the side of a square: " ))
#     area = side*side
#     perimeter = 4*side
#     print("Area of a square : ",area)
#     print("Perimeter of a square : ",perimeter)

# Method 2


class AreaSqr:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


s = int(input("Enter side value"))

s1 = AreaSqr(s)

print("Area of a square : ", s1.area())
print("Perimeter of a square : ", s1.perimeter())
