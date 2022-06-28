import numpy as np
arr = np.array(['New Delhi', 'Chennai', 'Bangalore', 'Hyderabad'])

# Print the len of each element array
arr_len = [len(i) for i in arr]
print(arr_len)

# swap case of string element in array
swap_arr = np.char.swapcase(arr)
print(swap_arr)


