import PyPDF2 as pp

numFiles = int(input("How many files do you want to join? "))
# pdfReader = pp.PdfFileReader()
pdfWriter = pp.PdfFileWriter()

for x in range(numFiles):
    fileName = input("Type name of file" + str(x+1) + "(without .pdf): ")# prompt name
    fileObj = open(fileName + '.pdf','rb')
    pdfReader = pp.PdfFileReader(fileObj)
    numPages = pdfReader.getNumPages()
    for y in range(numPages):
        pdfWriter.addPage(pdfReader.getPage(y))
    
outputName = input("Name the output file: ")
outputFile = open(outputName + '.pdf', 'wb')
pdfWriter.write(outputFile)
outputFile.close()
fileObj.close()

input("Press enter to close ")
