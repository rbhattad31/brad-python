List = ['apple-orange-apple', 'banana-grapes', 'fig-watermelons-pineapple', 'guava-guava']
print("The original list : " + str(List))
res = [set(sub.split('-')) for sub in List]
print("The list after duplicate removal : " + str(res))
