import os
import shutil
import errno
# Source Path
curr_path = os.getcwd()
source = os.path.join(curr_path, 'venv')

# Destination path
Destination = os.path.join(curr_path, 'venv_1')

# using try block to catch os error
try:
    shutil.copytree(source, Destination)
except OSError as err:
    if err.errno == errno.ENOTDIR:
        shutil.copy2(source, Destination)
    else:
        print("Error: % s" % err)