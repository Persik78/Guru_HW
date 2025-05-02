import zipfile
files = ['tmp/test_pdf2.pdf', 'tmp/test_xlsx.xlsx', 'tmp/test_csv.csv']

with zipfile.ZipFile('tmp/HW_zip_file_final.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for i in files:
        zip_file.write(i)