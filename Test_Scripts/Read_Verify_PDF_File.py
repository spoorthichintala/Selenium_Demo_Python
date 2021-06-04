import PyPDF2



file = open("EItin_DIXIT_BLR-AUH_TLWMAW43.pdf", "rb")
reader = PyPDF2.PdfFileReader(file)
# To read total number of pages of PDF file
print(reader.numPages)
# To extract text from first page
page1 = reader.getPage(0)
pdfData = page1.extractText()
print("Data from Page 1",page1.extractText())
assert "Abu Dhabi" in pdfData