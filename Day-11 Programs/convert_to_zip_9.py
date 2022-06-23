import os
import zipfile

# write all subdirectory and files in zip file
zf = zipfile.ZipFile("zipfile_1.zip", "w")
for directory, subdirectory, files in os.walk("venv"):
    zf.write(directory)
    for filename in files:
        zf.write(os.path.join(directory, filename))
zf.close()
