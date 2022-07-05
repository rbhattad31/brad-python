import zipfile
zip_files = zipfile.ZipFile('File-zip.zip', 'w')
zip_files.write('sample1.txt', compress_type=zipfile.ZIP_DEFLATED)
zip_files.write('sample2.txt', compress_type=zipfile.ZIP_DEFLATED)
zip_files.write('sample3.txt', compress_type=zipfile.ZIP_DEFLATED)
zip_files.write('sample4.txt', compress_type=zipfile.ZIP_DEFLATED)

# zip_files.write('C:\Python_D12', compress_type=zipfile.ZIP_DEFLATED)
