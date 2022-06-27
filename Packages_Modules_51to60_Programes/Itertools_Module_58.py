import itertools

counter = itertools.count()

data = [100, 200, 300, 400]
daily_data = list(zip(itertools.count(), data))
print(daily_data)

counter = itertools.cycle(('on', 'off'))
print(next(counter))
print(next(counter))

counter = itertools.repeat(2)
print(next(counter))
print(next(counter))


names = ['pramod','madhura']
combined = itertools.chain(names)
print(next(combined))

