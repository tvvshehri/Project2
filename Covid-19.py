import PyPDF2

pdf_file = open('Covid-19.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file)
page_num = pdf_reader.numPages
page = pdf_reader.getPage(page_num-1)
text = page.extractText()

file = open(r"C:\Users\tvvsh\OneDrive\Desktop\Project\\Covid-19.txt", "a")
file.writelines(text)
file.close()


