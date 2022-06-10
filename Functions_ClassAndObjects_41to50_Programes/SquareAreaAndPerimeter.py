class square:
    def __init__(self,a):
        self.side=a
    def area(self):
        return(self.side*self.side)
    def perimeter(self):
        return(4*self.side)
sq=square(6)
print("Area:",sq.area())
print("perimeter:",sq.perimeter())