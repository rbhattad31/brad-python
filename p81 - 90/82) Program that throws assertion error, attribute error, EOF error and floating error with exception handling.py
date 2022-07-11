# AssertionError
try:
	x = 1
	y = 0
	assert y != 0, "Invalid Operation"
	print(x / y)

except AssertionError as msg0:
	print(msg0)

else:
	print("No Exception")

finally:
	print("End1")


# AttributeError
class Greet:

	def __init__(self):
		self.a = 'Hello World'


obj = Greet()

try:
	print(obj.a)

	# Raises an AttributeError
	print(obj.b)

except AttributeError as msg:
	print(msg)

else:
	print("No Exception")

finally:
	print("End2")


# Name_Error_Message
def name_error_message():

	try:
		k = "Excel"
		print(kx)
		return y

	except Exception as msg1:
		print(msg1)

	finally:
		print("End3")


name_error_message()


# Floating point error
def floating_point_error():
	try:
		height = float(input('Enter your height (meters):'))  # fraction values produce vale error ex 1/3,4/7...
		weight = float(input('Enter your weight (kilograms):'))

	except ValueError as msg2:
		print(msg2)

	finally:
		print("End4")


floating_point_error()
