#!/usr/bin/env python3
"""
pdf_splitter.py
--by yash

Splits a PDF file into multiple parts based on provided page ranges.
Usage:
    python pdf_splitter.py -i input.pdf -o output_prefix -r "1-3,5-7"
Example:
    python pdf_splitter.py -i document.pdf -o split -r "1-3,5-7"
"""

import argparse
import sys
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_prefix, ranges):
    reader = PdfReader(input_pdf)
    for idx, prange in enumerate(ranges):
        start, end = prange
        writer = PdfWriter()
        for i in range(start - 1, end):
            try:
                writer.add_page(reader.pages[i])
            except IndexError:
                print(f"Page {i+1} does not exist in the PDF.", file=sys.stderr)
        output_file = f"{output_prefix}_part{idx+1}.pdf"
        with open(output_file, "wb") as f:
            writer.write(f)
        print(f"Created: {output_file}")

def parse_ranges(ranges_str):
    ranges = []
    parts = ranges_str.split(',')
    for part in parts:
        try:
            start, end = part.split('-')
            ranges.append((int(start), int(end)))
        except ValueError:
            print(f"Invalid range format: {part}", file=sys.stderr)
            sys.exit(1)
    return ranges

def main():
    parser = argparse.ArgumentParser(description="Split a PDF file by page ranges.")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file")
    parser.add_argument("-o", "--output", required=True, help="Output file prefix")
    parser.add_argument("-r", "--ranges", required=True, help="Comma-separated page ranges (e.g., '1-3,5-7')")
    args = parser.parse_args()
    ranges = parse_ranges(args.ranges)
    split_pdf(args.input, args.output, ranges)

if __name__ == "__main__":
    main()
