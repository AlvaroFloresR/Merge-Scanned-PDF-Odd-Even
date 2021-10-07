#Import Packages
import itertools as itt
import sys

#Include additional installed Packaged: https://pypi.org/project/PyPDF2/
import PyPDF2 as PDF



##########
## Main ##
##########
pdf_out = PDF.PdfFileWriter()

#Files to be merged need to be called
# even.pdf
# odd.pdf

with open("odd.pdf", 'rb') as read_odd:
    with open("even.pdf", 'rb')  as read_even:
        pdf_odd = PDF.PdfFileReader(read_odd,strict=False)
        pdf_even = PDF.PdfFileReader(read_even,strict=False)

        #Add pages after inversing the order of the odd file
        for page in itt.chain.from_iterable(itt.zip_longest(pdf_odd.pages, reversed(pdf_even.pages))):
            if page:
                pdf_out.addPage(page)
                
        #Create output file called "merged_doc.pdf"
        with open("merged_doc.pdf", 'wb') as file_out:
            pdf_out.write(file_out)
