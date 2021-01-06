"""
Prompts for the name of a .pdf file.
Returns the number of pages in that pdf.
"""

import PyPDF2
pdfFileName = input("type in pdf file name (not including .pdf): ")
pdfFileObj = open(pdfFileName + '.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("There are", pdfReader.numPages, "pages")
input()
