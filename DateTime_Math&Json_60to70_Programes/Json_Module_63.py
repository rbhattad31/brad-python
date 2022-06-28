import json

person_dict = {"name": "Pramod",
               "languages": ["English", "French"],
               "married": True,
               "age": 24
               }

with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)


person_string = '{"name": "Pramod", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent=4, sort_keys=True))
