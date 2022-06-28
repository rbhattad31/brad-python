import os.path

output = os.path.exists('Employee_data_xls.xls')
print(output)


def convert_bytes(size):
    global x
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0


f_size = os.path.getsize('Employee_data_xls.xls')
x = convert_bytes(f_size)
print('file size is', x)
