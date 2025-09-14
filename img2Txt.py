import os
import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import sys

# Point to Tesseract installation (update this path if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def open_file(filepath):
    """Open file with default program depending on OS"""
    if sys.platform.startswith("win"):
        os.startfile(filepath)  # Windows
    elif sys.platform == "darwin":
        subprocess.call(["open", filepath])  # macOS
    else:
        subprocess.call(["xdg-open", filepath])  # Linux

def main():
    # Create root window once and reuse it
    root = tk.Tk()
    root.withdraw()  # hide main window

    # Open folder picker for images
    image_folder = filedialog.askdirectory(title="Select the folder containing your images")

    if not image_folder:
        print("No folder selected. Exiting.")
        return

    # Open Save As dialog for output file
    output_path = filedialog.asksaveasfilename(
        title="Save extracted text as...",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if not output_path:
        print("No save location selected. Exiting.")
        return

    # Collect all images
    image_files = sorted([
        f for f in os.listdir(image_folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ])

    if not image_files:
        print("No images found in the selected folder.")
        return

    # Process each image
    with open(output_path, "w", encoding="utf-8") as out_file:
        for img_file in image_files:
            img_path = os.path.join(image_folder, img_file)
            try:
                text = pytesseract.image_to_string(Image.open(img_path))
                out_file.write(f"--- {img_file} ---\n")
                out_file.write(text.strip() + "\n\n")
                print(f"Processed {img_file}")
            except Exception as e:
                print(f"Error processing {img_file}: {e}")

    print(f"\n✅ Text extraction complete! File saved at: {output_path}")

    # Ask if the user wants to open the file
    if messagebox.askyesno("Open File?", f"Do you want to open the file now?\n\n{output_path}"):
        open_file(output_path)

    root.destroy()  # clean up Tkinter

if __name__ == "__main__":
    main()
