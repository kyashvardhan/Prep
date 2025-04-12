#!/usr/bin/env python3
"""
pdf_joiner.py

A simple PDF joiner utility that combines multiple PDF files into one file.

Usage:
    python pdf_joiner.py -o combined.pdf input1.pdf input2.pdf ... inputN.pdf
"""

import argparse
import sys
from PyPDF2 import PdfReader, PdfWriter

def join_pdfs(pdf_list, output_path):
    """Join multiple PDFs into a single PDF file."""
    pdf_writer = PdfWriter()
    
    for pdf_path in pdf_list:
        try:
            pdf_reader = PdfReader(pdf_path)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            print(f"Added: {pdf_path} ({len(pdf_reader.pages)} pages)")
        except Exception as e:
            print(f"Error reading {pdf_path}: {e}", file=sys.stderr)
    
    # Write the merged PDF to the output file.
    with open(output_path, "wb") as out_file:
        pdf_writer.write(out_file)
    print(f"Successfully created merged PDF: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Combine multiple PDF files into one.")
    parser.add_argument("-o", "--output", required=True, help="Output PDF file name.")
    parser.add_argument("pdfs", nargs="+", help="List of PDF files to join.")
    args = parser.parse_args()

    join_pdfs(args.pdfs, args.output)

if __name__ == "__main__":
    main()
