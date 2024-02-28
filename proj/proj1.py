import os
import tempfile
from PyPDF2 import PdfReader
import pytesseract

def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            # Extract text from each page
            page_text = reader.pages[page_num].extract_text()
            text += page_text + "\n"
    return text

def main():
    # Path to input PDF file
    pdf_file_path = '../../../../mnt/c/Users/KTIBREWA/Desktop/sample2.pdf'

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_file_path)

    # Path to output text file
    output_text_file = '../../../../mnt/c/Users/KTIBREWA/Desktop/output_text_file.txt'

    # Write extracted text to a text file
    with open(output_text_file, 'w', encoding='utf-8') as file:
        file.write(extracted_text)

    print("Text extracted successfully and saved to:", output_text_file)

if __name__ == "__main__":
    main()

