import json

#   import demjson

student = {"101": {"class": 'V', "Name": 'Rohit',  "Roll_no": 7},
           "102": {"class": 'V', "Name": 'David',  "Roll_no": 8},
           "103": {"class": 'V', "Name": 'Salman', "Roll_no": 12}}

print(json.dumps(student))

print(json.dumps(student, sort_keys=True))

tup1 = ('Red', 'Black', 'White')
print(json.dumps(tup1))

json_data = '{"103": {"class": "V", "Name": "salman", "Roll_n": 12},' \
            ' "102": {"class": "V", "Name": "David", "Roll_no": 8},' \
            ' "101": {"class": "V", "Name": "Rohit", "Roll_no": 7}}'

print(json.loads(json_data))

json_var = """
{
    "Country": {
        "name": "INDIA",
        "Languages_spoken": [
            {
                "names": ["Hindi", "English", "Bengali", "Telugu"]
            }
        ]
    }
}
"""
var = json.loads(json_var)

#   var1 = [{"Math": 50, "physics": 60, "Chemistry": 70}]
#   print(demjson.encode(var1))


#   var2 = '{"a":0, "b":1, "c":2, "d":3, "e":4}'
#   text = demjson.decode(var2)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

person_string = '{"name": "tim", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent=4, sort_keys=True))


def __decode_json_stream(document, pos=0, decoder=json.JSONDecoder(), NOT_WHITESPACE=None):
    while True:
        # Create json stream without whitespace
        match = NOT_WHITESPACE.search(document, pos)

        if not match:
            # No more data
            return
        pos = match.start()

        try:
            obj, pos = decoder.raw_decode(document, pos)
        except json.JSONDecodeError:
            raise Exception("Invalid json formatting")

        yield obj
