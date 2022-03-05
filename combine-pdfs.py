#! python3
# combine-pdfs.py - Combines all the PDFs in the current working directory into a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()


# Find all PDF files in the current working directory
# Sort the filenames so the PDFs are added in order
# Write each page, excluding the first page, of each PDF to theoutput file

# Call os.listdir() to find all the files in the working directory andremove any non-PDF files.
# Call Python’s sort() list method to alphabetize the filenames
# Create a PdfFileWriter object for the output PDF
# Loop over each PDF file, creating a PdfFileReader object for it
# Loop over each page (except the first) in each PDF file
# Add the pages to the output PDF
# Write the output PDF to a file named allminutes.pdf