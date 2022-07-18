from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = 'Song.pdf'
pdf = PdfFileReader(file_path)

with open('Song.txt', 'w') as f:
    for page_num in range(pdf.numPages):
        page = pdf.getPage(page_num)

        try:
            txt= page.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100,'-'))
            f.write(txt)
    f.close()
