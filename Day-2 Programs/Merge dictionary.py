

def Merge(dict1, dict2):
    return (dict1.update(dict2))

dict1 = {'a':'apple', 'b':'orange'}
dict2 = {'d':'grapes', 'c':'coconut'}
print("Dictionar 1:",dict1)
print("Dictionar 2:",dict2)
print(Merge(dict1, dict2))
print(dict1)