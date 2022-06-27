import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [5, 6, 7, 8, 9],
                [2, 1, 5, 7, 8],
                [2, 9, 3, 1, 0]])

sum_2d = arr.sum(axis=0)

print("Column wise sum is :\n", sum_2d)