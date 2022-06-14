class square:
    def __init__(self, a):
        self.side = a
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side
n=square(7)
print(n.area())
print(n.perimeter())