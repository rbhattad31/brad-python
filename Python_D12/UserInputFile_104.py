file1 = open("myfile.txt", "a")  # append mode
file1.write("When the file is opened in append mode, the handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data. Let’s see the below example to clarify the difference between write mode and append mode.")
file1.close()
