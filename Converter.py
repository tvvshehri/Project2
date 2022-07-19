import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

def pdf2txt(PDF_File, TXT_File):
    File= open(PDF_File, 'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr, retData, laparams=LAParams())
    interpreter= PDFPageInterpreter(resMgr, TxtConverter)
    for page in PDFPage.get_pages(File):
        interpreter.process_page(page)

    txt = retData.getvalue()
    with open(TXT_File, 'w', encoding="utf-8") as f:
        f.write(txt)

PDF_File = 'Converter.pdf'
TXT_File = 'Converter.txt'
pdf2txt(PDF_File, TXT_File)
