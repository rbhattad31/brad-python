#pass by value
def set_list(list):
	list = ["P", "R", "A","M","O",]
	return list

#pass by reference
def add(list):
	list.append("D")
	return list
list_1 = []

#Function in Function
print(add(set_list(list_1)))

#lambda functions/Ananymous function
double = lambda x: x * 2
print(double(3))