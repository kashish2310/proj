import csv
import re
from PyPDF2 import PdfReader

def extract_sentences(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        
        # Extract text from each page
        full_text = ''
        for page in reader.pages:
            full_text += page.extract_text()
    
    # Split text into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', full_text)
    return sentences

def save_to_csv(sentences_list, csv_path):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ID', 'Sentence'])
        for book, sentences in sentences_list.items():
            for i, sentence in enumerate(sentences, start=1):
                csv_writer.writerow([i, sentence])

def main():
    pdf1_path = '../data/book/firstbook.pdf'  # Change this to the path of your first PDF file
    pdf2_path = '../data/book/secondbook.pdf'  # Change this to the path of your second PDF file
    csv_path = '../../../../mnt/c/Users/KTIBREWA/Desktop/output_sentences.csv'  # Change this to your desired CSV output path
    
    sentences_list = {}
    sentences_list['Book 1'] = extract_sentences(pdf1_path)
    sentences_list['Book 2'] = extract_sentences(pdf2_path)
    
    save_to_csv(sentences_list, csv_path)
    print(f"Sentences from both books have been extracted and saved to '{csv_path}'.")

if __name__ == "__main__":
    main()

