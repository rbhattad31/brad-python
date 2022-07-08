import numpy

arr = numpy.array([[1, 6, 5], [4, 6, 5], [3, 5, 2], [7, 5, 4]])

# checking for count of sequence (1, 6)
Number_of_sequences = repr(arr).count("1, 6")

print(Number_of_sequences)
