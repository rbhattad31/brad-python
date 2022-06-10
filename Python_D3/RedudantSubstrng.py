list = ['aa-aa-bb', 'bb-cc', 'gg-ff-gg', 'hh-hh']


print("The original list : " + str(list))


res = [set(sub.split('-')) for sub in list]


print("The list after duplicate removal : " + str(res))