import zipfile
target = 'File-zip.zip'
handle = zipfile.ZipFile(target)
for x in handle.namelist():
    if x.endswith('.txt'):
        handle.extract(x, 'File-zip')
