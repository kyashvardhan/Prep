#!/usr/bin/env python3
"""
pdf_info.py

Displays basic information and metadata from a PDF file.
Usage:
    python pdf_info.py -i input.pdf
"""

import argparse
from PyPDF2 import PdfReader

def dump_info(input_pdf):
    reader = PdfReader(input_pdf)
    info = reader.metadata
    num_pages = len(reader.pages)
    print(f"File: {input_pdf}")
    print(f"Number of pages: {num_pages}")
    print("Metadata:")
    if info:
        for key, value in info.items():
            print(f"  {key}: {value}")
    else:
        print("  No metadata found.")

def main():
    parser = argparse.ArgumentParser(description="Dump PDF metadata and info")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file")
    args = parser.parse_args()
    dump_info(args.input)

if __name__ == "__main__":
    main()
