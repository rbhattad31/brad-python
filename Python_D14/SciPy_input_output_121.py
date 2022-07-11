try:
    import scipy.io as syio

    n = int(input("Enter any number"))
    syio.savemat('num.mat', {'num': n})

    # Load the mat File
    matlab_file_contents = syio.loadmat('num.mat')
    print(matlab_file_contents)

    # printing the contents of mat file.
    matlab_file_contents = syio.whosmat('num.mat')
    print(matlab_file_contents)

    # Save the mat file
    string = input("Enter the string")
    syio.savemat('str.mat', {'str': string})

    # Load the mat File
    matlab_file_contents = syio.loadmat('str.mat')
    print(matlab_file_contents)

    # printing the contents of mat file.
    matlab_file_contents = syio.whosmat('str.mat')
    print(matlab_file_contents)

except:
    print("Something went wrong!,Please check the code")
