from zipfile import ZipFile

with ZipFile('tmp/test_archive.zip') as zip_file:
    print(zip_file.namelist())
