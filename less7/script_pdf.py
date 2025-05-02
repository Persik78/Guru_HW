import os.path

from pypdf import PdfReader

def test_pdf():
    reader = PdfReader('tmp/test_pdf2.pdf')

    print(len(reader.pages))
    print(reader.pages[0].extract_text())
    assert 'Test_pdf1' in reader.pages[0].extract_text()
    assert os.path.getsize('tmp/test_pdf2.pdf') == 188074