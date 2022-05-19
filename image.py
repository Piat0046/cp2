import fitz
import os
file_list = os.listdir('pdf')
print(file_list)
for pdffile in file_list:
    if 'pdf' in pdffile:
        file_name = pdffile.split('.')[0]
        doc = fitz.open(f"pdf\\{pdffile}")
        
        for num in range(len(doc)):
            page = doc.loadPage(num)  # number of page
            pix = page.getPixmap()
            output = f"{file_name}_{num}.png"
            pix.writePNG("pdf\\pdf_to_image\\" + output)
    