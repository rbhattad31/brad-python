Marks = {'Ram': 30, 'Teja': 29, 'Nikhil': 31, 'Jagan': 43, 'Madhu': 32, 'Raj': 38}
Value = 35

if Value in Marks.values():
    print('Value exists')
else:
    print('Value doesn\'t exist')

result = sorted(Marks.values())
print(result)


