import os
import io
import json
import fitz #PyMuPDF
from PIL import Image, ImageOps #Image Processing
import pytesseract #Python wrapper for Tesseract OCR


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PDF_DIR = os.path.join(BASE_DIR, "data")
OUT_DIR = os.path.join(BASE_DIR, "data", "output")
OUT_FILE = os.path.join(OUT_DIR, "exams_raw.json")

os.makedirs(OUT_DIR, exist_ok=True)

def render_for_ocr(page, dpi=400):
    pix = page.get_pixmap(dpi=dpi)  #Turn the PDF page into an image (higher DPI = clearer image)
    img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("L")#Convert to grayscale (OCR doesn’t need colour)
    img = ImageOps.autocontrast(img)#Improve contrast so text stands out more
    w, h = img.size
    img = img.resize((int(w * 1.5), int(h * 1.5)))#Make the image slightly bigger to help OCR read small text
    return img

def ocr_page(page):
    img = render_for_ocr(page)#Prepare the page image for OCR
    #Different layout settings in Tesseract
    configs = [
        "--oem 1 --psm 6",#Block of text
        "--oem 1 --psm 4",#Columns
        "--oem 1 --psm 3",#Automatic layout
    ]
    best = ""
    for cfg in configs: #Try each Tesseract setting one by one.
        txt = pytesseract.image_to_string(img, lang="eng", config=cfg).strip()#Read the image and give back text
        if len(txt) > len(best): #Result has more characters than the one we saved before,keep
            best = txt
    return best

papers = []

for name in sorted(os.listdir(PDF_DIR)):
    if not name.lower().endswith(".pdf"):
        continue

    path = os.path.join(PDF_DIR, name)
    print(f"Processing {name}")

    doc = fitz.open(path)
    pages = []
    combined = []

    for i in range(doc.page_count):
        page = doc.load_page(i)

        extracted = page.get_text("text").strip()
        ocr_text = ocr_page(page)

        if len(ocr_text) > len(extracted):
            chosen = ocr_text
            method = "ocr"
        else:
            chosen = extracted
            method = "text"

        pages.append({
            "page": i + 1,
            "method": method,
            "length": len(chosen),
            "text": chosen
        })
        combined.append(chosen)

    papers.append({
        "paper": name,
        "page_count": doc.page_count,
        "pages": pages,
        "text": "\n".join(combined)
    })

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(papers, f, ensure_ascii=False, indent=2)

print("Saved:", OUT_FILE)
