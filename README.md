# Image to Text OCR

A simple Python script that uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) to extract text from images (e.g., book screenshots) and save the results into a single text file.  

This project is useful if you want to quickly convert multiple images (like textbook pages or scanned notes) into editable text.  

---

## Features

- Select a folder containing your images (via popup file dialog).  
- Automatically extracts text from `.png`, `.jpg`, and `.jpeg` files in order.  
- Choose where to save the output text file with a **Save As** popup.  
- Text is grouped by image filename for clarity.  
- Option to **open the generated file immediately** when processing completes.  

---

## Requirements

- Python 3.8 or higher  
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system  
- The following Python packages:  
  ```bash
  pip install pytesseract pillow

Setup

Install Tesseract OCR
.

On Windows, the default path is usually:

C:\Program Files\Tesseract-OCR


Make sure to update the script if your install path is different.

Clone this repository or download the script.

Open the project in your IDE (e.g., PyCharm).

Install the required Python packages:

pip install pytesseract pillow

Usage

Run the script:

python img2Txt.py


When prompted:

Select the folder containing your screenshots/images.

Choose a name and location for the output .txt file.

The script will process each image in order and save all extracted text into the single text file you chose.

After completion, you’ll be asked:

“Do you want to open the file now?”
If you select Yes, the file will open in your default text editor.

Example

Input folder contents:

Ch7 - 201.png
Ch7 - 202.png
Ch7 - 203.png


Output file (book_text.txt):

--- Ch7 - 201.png ---
[Extracted text here]

--- Ch7 - 202.png ---
[Extracted text here]

--- Ch7 - 203.png ---
[Extracted text here]

Notes

Images are processed in sorted order by filename.

Only .png, .jpg, and .jpeg files are supported.

You can ignore generated text files and images in GitHub by using the provided .gitignore.

License

This project is open-source and free to use under the MIT License.