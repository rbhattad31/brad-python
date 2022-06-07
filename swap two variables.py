#Python program to swap two variables
x=5
y=10
#To take inputs from the user
#x=input('Enter value ofx:')
#y=input('Enter value ofy:')
#createatemporary variable and swap the values
temp=x
x=y
y=temp
print('The value ofxafter swapping:{}'.format(x))
print('The value ofyafter swapping:{}'.format(y))