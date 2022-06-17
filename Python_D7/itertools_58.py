import itertools

counter = itertools.count()
# for num in counter:
# print(num)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter1 = itertools.count(start=5, step=5)
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))

data = [101, 202, 550, 1922]
res_data = list(zip(itertools.count(), data))
print(res_data)

res_data2 = list(itertools.zip_longest(range(10), data))
print(res_data2)

counter2 = itertools.cycle([1, 2, 3])
print(next(counter2))
print(next(counter2))
print(next(counter2))
print(next(counter2))

counter3 = itertools.repeat('Bradsol')
print(next(counter3))
print(next(counter3))
print(next(counter3))
print(next(counter3))

squares = map(pow, range(15), itertools.repeat(2))
print(list(squares))

squares1 = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
print(list(squares1))

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
names = ['Sai', 'Akhil', 'Arya']

result = itertools.combinations(letters, 2)

for items in result:
    print(items)

result2 = itertools.permutations(letters, 2)

for item in result2:
    print(item)


