#write a program to demonstrate File Input / Output package functions in scipy.io

import scipy.io as syio

# Save the mat file
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
syio.savemat('arr.mat', {'arr': arr})

# Load the mat File
matlab_file_contents = syio.loadmat('arr.mat')
print(matlab_file_contents)

# printing the contents of mat file.
matlab_file_contents = syio.whosmat('arr.mat')
print(matlab_file_contents)