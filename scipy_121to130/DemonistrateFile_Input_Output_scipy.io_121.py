import scipy.io as sy
import numpy as np

# Save the mat file with array
arr = np.arange(10).reshape(5, 2)
sy.savemat('num.mat', {'num': arr})

# Load the mat File
file_contents = sy.loadmat('num.mat')
print(file_contents)

# printing the contents of mat file.
file_contents = sy.whosmat('num.mat')
print(file_contents)

# saving string file
str_1 = 'Hi Guys'
sy.savemat('str.mat', {'str': str_1})
file_contents = sy.loadmat('str.mat')
print(file_contents)
matlab_file_contents = sy.whosmat('str.mat')
print(file_contents)