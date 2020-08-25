import PyPDF2 as pp

while True: # begin loop

    print("This is the PDF multitool.\n") # would user like to:
    print("To split a pdf into pages, type \"split\"\n") # split a pdf into pages
    print("To extract a page or pages, type \"extract\"\n") # extract a page (or pages)
    print("To join several pdfs, type \"join\"\n") # join several PDFs together
    tool = input("\nSelect a tool: ") # get input

    # if split
    # get number of pages
    # loop and create a copy of each page

    # if extract
    # prompt how many pages to extract
    # loop and prompt for number of each page

    # if join
    # prompt for number to join together
    # loop and prompt for each file name, adding them to the list

    done = input("Are you finished? y/n: ") # prompt whether done
    if done == 'y': # if yes, end loop
        break
    # if no, return to beginning



