import PyPDF2 as pp

sourceName = input("type in pdf file name (not including .pdf): ")# prompt for a pdf name
source = open(sourceName + '.pdf', 'rb') # open as readable binary
sourceReader = pp.PdfFileReader(source) # store to reader object
pdfWriter = pp.PdfFileWriter() 
inRange = input("Are the pages in the same range? (y/n): ") # prompt if pages are in a range together
num = 0;
if inRange == 'y':
    firstPage = int(input("First Page to extract: ")) # prompt for first page in range
    lastPage = 1 + int(input("Last Page to extract: ")) # prompt for last page in range
    num = lastPage - firstPage
    for x in range(num): # for number of pages
                pdfWriter.addPage(sourceReader.getPage(x + firstPage)) # extract page
else: 
    num = int(input("Number of pages to extract: ")) # prompt for number of pages to extract
    for x in range(num): # for number of pages
        pageNum = input("\n" + str(x+1) + "th page to extract: ") # prompt for page number
        pdfWriter.addPage(sourceReader.getPage(int(pageNum))) # extract page


outputName = input("Name the output file: ") # prompt for a name
outputFile = open(outputName + '.pdf', 'wb') # open new pdf
pdfWriter.write(outputFile) # write to new pdf
outputFile.close() # close pdf
source.close();

input("Press enter to close ")
