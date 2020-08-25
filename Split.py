import PyPDF2 as pp

targetFile = input("Name the file you want to split (without .pdf):")
target = open(targetFile + '.pdf', 'rb') 
pdfReader = pp.PdfFileReader(target)
numPages = pdfReader.getNumPages()
for x in range(numPages):
    pdfWriter = pp.PdfFileWriter()
    fragment = open(targetFile + str(x+1) + '.pdf','wb')
    pdfWriter.addPage(pdfReader.getPage(x))
    pdfWriter.write(fragment)
    fragment.close()
target.close()

input("Press enter to close ")
    
