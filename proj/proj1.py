import re
import csv
#import PyPDF2#
import pdfplumber

def split_sentences(text):
    sentences = re.split(r'\.\s*', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences

def extract_text_from_pdf(pdf_file_path):
    text = ""
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    print("Extracted Text:", text)  
    return text

def write_to_csv(sentences, csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([' id ',' sentence '])
        for i, sentence in enumerate(sentences):
            writer.writerow([i  ,  sentence])

def main():
    # Read text from a PDF file
    pdf_file_path = '../data/book/sample.pdf'  # Replace 'sample_pdf.pdf' with your PDF file path
    text = extract_text_from_pdf(pdf_file_path)

    # Split the text into sentences
    sentences = split_sentences(text)

    # Print the number of sentences
    print("Number of sentences:", len(sentences))

    # Print the sentences
    for i, sentence in enumerate(sentences):
        print(i, sentence)

    # Write sentences to CSV

    write_to_csv(sentences, 'sentences.csv')

if __name__ == "__main__":
    main()

