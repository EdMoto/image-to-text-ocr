import os
from PIL import Image
import pytesseract

# Windows users: make sure this points to your Tesseract install
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_images(image_folder, output_name):
    output_file = os.path.join(image_folder, output_name)

    with open(output_file, "w", encoding="utf-8") as f:
        # Sort to keep pages in order
        for img_name in sorted(os.listdir(image_folder)):
            if img_name.lower().endswith((".png", ".jpg", ".jpeg")):
                img_path = os.path.join(image_folder, img_name)
                print(f"Processing {img_name}...")

                text = pytesseract.image_to_string(Image.open(img_path))
                f.write(f"\n\n--- {img_name} ---\n\n")
                f.write(text)

    print(f"\n✅ Text extraction complete. Saved to: {output_file}")

if __name__ == "__main__":
    folder = input("Enter the path to the folder with your images: ").strip()
    if os.path.isdir(folder):
        output_name = input("Enter a name for the output text file (default: book_text.txt): ").strip()
        if not output_name:
            output_name = "book_text.txt"
        elif not output_name.lower().endswith(".txt"):
            output_name += ".txt"

        extract_text_from_images(folder, output_name)
    else:
        print("❌ Invalid folder path. Please try again.")
