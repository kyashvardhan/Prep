#!/usr/bin/env python3
"""
pdf_text_extractor.py
--by yash
Extracts text from a PDF file and saves it to a text file.
Usage:
    python pdf_text_extractor.py -i input.pdf -o output.txt
"""

import argparse
from PyPDF2 import PdfReader

def extract_text(input_pdf, output_txt):
    reader = PdfReader(input_pdf)
    all_text = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text.append(text)
    full_text = "\n".join(all_text)
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Extracted text saved to {output_txt}")

def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF file")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file")
    parser.add_argument("-o", "--output", required=True, help="Output text file")
    args = parser.parse_args()
    extract_text(args.input, args.output)

if __name__ == "__main__":
    main()
