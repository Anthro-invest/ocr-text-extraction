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
