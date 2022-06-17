# product
from itertools import product
a= [1,2]
b= [3,4]
prod = product(a,b)
print(list(prod))

# permutations
from itertools import permutations
a =[1,2,3]
perm = permutations(a)
print(list(perm))

# combinations
from itertools import combinations, combinations_with_replacement
b= [1,2,3,4]
comb= combinations(b,3)
print(list(comb))
comb_r = combinations_with_replacement(b,2)
print(list(comb_r))

# accumulate operations(Sum, Mul)
from itertools import accumulate
import operator
c = [1,2,3,4]
acc_sum = accumulate(c)
acc_mul = accumulate(c, func = operator.mul)
print(list(acc_mul))
print(list(acc_sum))

# group by
from itertools import groupby
def smaller_than_3(x):
    return x<3
a =[1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key , value in group_obj:
    print(key, list(value))

# infinite iterators
from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i==16:
        break
a = [1,2,3,4]
# cycles the same list again and again
for i in cycle(a):
    print(i)
    if i == 4:
        break
# repeats the same number
for i in repeat(0):
    print(i)
