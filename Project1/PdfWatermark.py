import PyPDF2

with open('F:/Python/PCProjects/pdf/twopage.pdf', mode='rb') as file:
    with open('F:/Python/PCProjects/pdf/wtr.pdf', mode='rb') as wt_file:
        reader = PyPDF2.PdfFileReader(file)
        reader1 = PyPDF2.PdfFileReader(wt_file)
        page2 = reader1.getPage(0)
        page_numbers = reader.getNumPages()
        i = 0
        writer = PyPDF2.PdfFileWriter()
        print(page_numbers)
        while i < int(page_numbers):
            page1 = reader.getPage(i)
            page1.mergePage(page2)
            writer.addPage(page1)
            i += 1

        with open('F:/Python/PCProjects/pdf/test2.pdf', mode='wb') as new_file:
            writer.write(new_file)
