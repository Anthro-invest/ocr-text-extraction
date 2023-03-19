# ocr-text-extraction

this script is about extracting text from a batch of images and pasting it to a text file. Below is the code generated from GPT4. Does it work?

To achieve this, you can use the pytesseract library, which is a Python wrapper for Google's Tesseract-OCR Engine. First, you need to install it using pip:


pip install pytesseract
You also need to install Tesseract itself. You can find installation instructions for your operating system here: https://github.com/tesseract-ocr/tesseract

After you've installed both Tesseract and pytesseract, you can use the following script to extract text from images in batches:

python
Copy code
import os
import sys
from PIL import Image
import pytesseract

def extract_text(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def batch_extract_text(image_paths, output_path):
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for image_path in image_paths:
            text = extract_text(image_path)
            if text is not None:
                output_file.write(f"Text from {image_path}:\n")
                output_file.write(text)
                output_file.write("\n\n")

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <output_file> <input_image1> <input_image2> ...")
        return

    output_path = sys.argv[1]
    image_paths = sys.argv[2:]
    batch_extract_text(image_paths, output_path)

if __name__ == "__main__":
    main()
Save the script as batch_image_text_extraction.py and run it with a list of image files you want to process:

sh
Copy code
python batch_image_text_extraction.py output.txt image1.png image2.jpg image3.bmp
This script takes an output file path as the first argument and then a list of input image files. It processes the images one by one, extracts the text, and writes the text to the output file.
