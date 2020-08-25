import PyPDF2
pdfFileName = input("type in pdf file name (not including .pdf): ") # get the pdf filename
pdfFileObj = open(pdfFileName + '.pdf', 'rb') # open the pdf file to an object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # create reader object from the pdf object
pdfWriter = PyPDF2.PdfFileWriter() # create writer object
pageNum = input("type in page to copy: ") # get page to copy
pageObj = pdfReader.getPage(int(pageNum)) # open page through the pdf reader object
pdfWriter.addPage(pageObj) # add page to writer object
pdfOutputFile = open(pdfFileName + 'pg' + pageNum + '.pdf', 'wb') # open an output file as a writeable binary
pdfWriter.write(pdfOutputFile) # use write method on writer object to write to output file
pdfOutputFile.close() # close output file
pdfFileObj.close() # close input file
