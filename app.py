import os
from PyPDF2 import PdfFileMerger

location = input("Digite o local da pasta onde estao os pdfs: ")

pdfFiles = [location + '\\' + file for file in os.listdir(location) if file.endswith(".pdf")]
print(pdfFiles)

merger = PdfFileMerger()
for pdf in pdfFiles:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as finalPdf:
    merger.write(finalPdf)