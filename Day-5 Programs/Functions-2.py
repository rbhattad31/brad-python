#pass by value
def set_list(list):
	list = ["A", "B", "C"]
	return list
#pass by reference
def add(list):
	list.append("D")
	return list
list_1 = []
#Function in Function
print(add(set_list(list_1)))



