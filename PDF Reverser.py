import PyPDF2 as pp

sourceName = input("Name of the file you want to reverse (without .pdf): ")
sourceObj = open(sourceName + '.pdf','rb')
pdfReader = pp.PdfFileReader(sourceObj)
pdfWriter = pp.PdfFileWriter()

numPages = pdfReader.getNumPages()

for x in range(numPages):
    page = pdfReader.getPage((numPages - 1) - x)
    pdfWriter.addPage(page)

newObj = open(sourceName + ' backwards.pdf','wb')
pdfWriter.write(newObj)
newObj.close()
sourceObj.close()

input("Press enter to close ")
