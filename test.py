import requests
import fitz
import io
from PIL import Image

num = 2000
while True:
    URL = f"https://pdf.etoday.co.kr/daily/pdf/detoday0{num}.pdf"
    file = requests.get(URL, stream = True)
    if file.status_code == 200:
        print('성공')
        with open(f"{num}.pdf","wb") as pdf:
            for chunk in file.iter_content(chunk_size=1024):
        
                if chunk:
                    pdf.write(chunk)
                    # name = fitz.open(f'2000.pdf')
                    # for page_number in range(len(name)):
                    #     page = pdf_file[page_number]
                    #     list_image = page.getImageList()
                        
                    #     if list_image:
                    #         print(f"{len(list_image)} images found on page {page_number}")
                    #     else:
                    #         print("No images found on page", page_number)


        num += 1

    else:
        print('실패')
        break