#!/usr/bin/env python3
"""
pdf_protector.py
--by yash
Applies password protection to a PDF file.
Usage:
    python pdf_protector.py -i input.pdf -o protected.pdf -p mypassword
"""

import argparse
from PyPDF2 import PdfReader, PdfWriter

def protect_pdf(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt(password)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Password-protected PDF saved as {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Apply password protection to a PDF file")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file")
    parser.add_argument("-o", "--output", required=True, help="Output PDF file")
    parser.add_argument("-p", "--password", required=True, help="Password for protection")
    args = parser.parse_args()
    protect_pdf(args.input, args.output, args.password)

if __name__ == "__main__":
    main()
