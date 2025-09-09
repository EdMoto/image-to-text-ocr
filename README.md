# Image to Text (OCR) Script

This Python script extracts text from images (such as screenshots of book pages) and saves everything into a single text file.  
It uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) through the `pytesseract` library.

---

## Features
- Extracts text from `.png`, `.jpg`, and `.jpeg` images.
- Processes files in order (sorted by filename).
- Lets you choose your output text file name.
- Saves the results directly into the same folder as your images.

---

## Requirements
- **Python 3.x**
- **Tesseract OCR** installed on your system  
  - [Windows installer (UB Mannheim builds)](https://github.com/UB-Mannheim/tesseract/wiki)  
  - Mac: `brew install tesseract`  
  - Linux: `sudo apt install tesseract-ocr`
- Python packages (install with pip):
  ```bash
  pip install pillow pytesseract
Usage

Save your screenshots in a folder (e.g., C:\Users\You\Documents\BookScreenshots).

Run the script:

python img2Txt.py


Enter:

The folder path containing your images.

A name for the output text file (default: book_text.txt).

The script will process the images in order and save the text file into the same folder.

Example

Input folder:

Ch7 - 201.png
Ch7 - 202.png
Ch7 - 203.png


Output file: book_text.txt

--- Ch7 - 201.png ---
[Extracted text here]

--- Ch7 - 202.png ---
[Extracted text here]

--- Ch7 - 203.png ---
[Extracted text here]

Notes

If Tesseract is not found automatically on Windows, update the script with the correct path:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


Use consistent filenames (e.g., Ch7 - 201.png, Ch7 - 202.png) to ensure pages are processed in the correct order.
