import zipfile

target_dir = 'New'

# Unzip directory

with zipfile.ZipFile("file4.txt.zip", "r") as zip_ref:
    zip_ref.extractall(target_dir)
