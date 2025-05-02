from zipfile import ZipFile, ZIP_STORED

ZipFile('tmp/test_zip.zip','x', compression=ZIP_STORED)
