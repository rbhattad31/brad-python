def recurSum(Add):
    if Add <= 1:
        return Add
    return Add + recurSum(Add - 1)

n = int(input())
print(recurSum(n))