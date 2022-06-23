import json
# This function converts the object into JSON format.
data=['Rakesh',{'marks':(50,60,70)}]
s=json.dumps(data)
print(s)
# serializes Python objects into JSON format
e=json.JSONEncoder()
e.encode(data)
print(e)
# decoded in json string back to Python data structure.
d=json.JSONDecoder()
d.decode(s)
print(d)

x ='{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



