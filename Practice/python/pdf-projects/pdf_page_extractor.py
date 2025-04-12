#!/usr/bin/env python3
"""
pdf_page_extractor.py
--by yash

Extracts specified pages from a PDF and saves them as a new PDF.
Usage:
    python pdf_page_extractor.py -i input.pdf -o output.pdf -p "1,3,5"
"""

import argparse
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, pages):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for p in pages:
        try:
            writer.add_page(reader.pages[p - 1])
        except IndexError:
            print(f"Page {p} does not exist in {input_pdf}.")
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Extracted pages saved in {output_pdf}")

def parse_pages(pages_str):
    return [int(p.strip()) for p in pages_str.split(",")]

def main():
    parser = argparse.ArgumentParser(description="Extract specific pages from a PDF")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file")
    parser.add_argument("-o", "--output", required=True, help="Output PDF file")
    parser.add_argument("-p", "--pages", required=True, help="Comma-separated list of pages to extract (e.g., '1,3,5')")
    args = parser.parse_args()
    pages = parse_pages(args.pages)
    extract_pages(args.input, args.output, pages)

if __name__ == "__main__":
    main()
