import json


list1 = {"name": "vinoth", "age": 22, "city": "Madurai"}
# convert into JSON[ we can convert may data types to json string]
y = json.dumps(list1)
print(y)

# write to json file
content = {"Subjects": {"Maths": 85, "Physics": 90}}
with open("Sample.json", "w") as file:
    json.dump(content, file)

# read file
with open("Sample.json", "r") as file:
    data = json.load(file)
    print(data)

# indent json string
print(json.dumps(content, indent=1, sort_keys=True))

# Datatypes support in json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
