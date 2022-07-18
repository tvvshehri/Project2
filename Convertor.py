from PyPDF2 import PdfFileReader

doc = PdfFileReader("Convertor.pdf")

pages = doc.getNumPages()

f = open('Convertor.txt', 'w')

for i in range(pages):
    current_page = doc.getPage(i)
    text = current_page.extractText()
    f.write(text)

f.close()