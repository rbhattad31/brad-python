class Square:
    def __int__(self):
        self.x = ""

    @staticmethod
    def area():
        x = int(input("Enter the length of the square: "))
        area = x * x
        print("The area of the square is :", area)

    @staticmethod
    def perimeter():
        y = int(input("Enter the length of the square: "))
        perimeter = 4 * y
        print("The perimeter of the square is :", perimeter)


parameter = Square()
parameter.area()
parameter.perimeter()
