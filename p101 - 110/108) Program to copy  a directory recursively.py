import shutil


def copy_directory(src, des):

    try:
        shutil.copytree(src, des)

# Directories are the same error
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)

# Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

    finally:
        print('Process finished')


# Assigning source directory

src1 = 'New'

# Assigning source directory

des1 = 'New1'

# Function call
copy_directory(src1, des1)
