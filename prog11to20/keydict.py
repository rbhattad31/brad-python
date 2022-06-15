my_dict = {'x':int(input('enter number1: ')), 'y':int(input('enter number2: ')), 'z':int(input('enter number3: '))}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])