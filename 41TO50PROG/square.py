class square:
    def __init__(s1,a):
        s1.side=a
    def area(s1):
        return(s1.side*s1.side)
    def perimeter(s1):
        return(4*s1.side)
sq=square(int(input('enter side :')))
print("Area:",sq.area())
print("perimeter:",sq.perimeter())