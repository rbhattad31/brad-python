import cmath

a = int(input( 'enter a value:' ))
b = int(input( 'enter b value:' ))
c = int(input( 'enter c value:' ))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
x = (-b-cmath.sqrt(d))/(2*a)
y = (-b+cmath.sqrt(d))/(2*a)

print('x , y is : ',(x ,y))