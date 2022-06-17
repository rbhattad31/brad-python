import itertools
l1 = [2, 3, 4]
l2 = [[1, 2, 3], [4, 5, 6]]

# Combination
print(list(itertools.combinations(l1, 2)))
# Combination with replacement
print(list(itertools.combinations_with_replacement(l1, 3)))
# Permutation
print(list(itertools.permutations(l1)))
# chain list
chain_list = itertools.chain.from_iterable(l2)
print(list(chain_list))
