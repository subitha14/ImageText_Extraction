mport fitz  # PyMuPDF
import os
import cv2
import pytesseract
import io
from PIL import Image
visited = dict()

# Path to the PDF file
pdf_path = 'C:\Image Extraction\PDF\BODAS-Basics-IntroToXCPonCAN_short (1).pdf'                                                                                                                                                            

# Output folder
output_folder = 'C:\Image Extraction\output'
os.makedirs(output_folder, exist_ok=True)

# Open the PDF file
pdf_document = fitz.open(pdf_path)

pdf_name = os.path.basename(pdf_path)

print(pdf_name)

# Iterate through each page
for page_number in range(len(pdf_document)):
    # Get the page
    page = pdf_document.load_page(page_number)
    
    # Render the page to an image
    pix = page.get_pixmap()

    # Save the image
    # image_path = os.path.join(output_folder, f'page_{page_number + 1}.png')
    
    image_bytes = pix.tobytes("png")
    image = Image.open(io.BytesIO(image_bytes))
    # pix.save(image_path)

    # img = cv2.imread(image_path)
    config = ('-l eng --oem 1 --psm 3')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Image Extraction/TESSERACT/tesseract.exe'
    text = pytesseract.image_to_string(image, config=config)
    print(text)
    page = prepare_file(page_number,text,pdf_name)
    print(page)
    visited[page[4]] = page
print(visited)   
pages = sorted(visited.values())  
save_extracted_pages(pages) 

print(f"Saved {len(pdf_document)} pages as images in {output_folder}")
