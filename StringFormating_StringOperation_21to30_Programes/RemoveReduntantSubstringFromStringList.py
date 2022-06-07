test_list = ['aa-aa-bb', 'bb-cc', 'gg-ff-gg', 'hh-hh']
print("The original list : " + str(test_list))
res = [set(sub.split('-')) for sub in test_list]
print("The list after duplicate removal : " + str(res))