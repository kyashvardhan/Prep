#!/usr/bin/env python3
"""
pdf_watermarker.py
--by yash

Overlays a watermark from a separate single-page PDF onto each page of an input PDF.
Usage:
    python pdf_watermarker.py -i input.pdf -w watermark.pdf -o watermarked.pdf
"""

import argparse
from PyPDF2 import PdfReader, PdfWriter

def add_watermark(input_pdf, watermark_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    watermark = PdfReader(watermark_pdf).pages[0]
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(watermark)
        writer.add_page(page)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Watermarked PDF saved as {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Add a watermark to a PDF")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file")
    parser.add_argument("-w", "--watermark", required=True, help="Watermark PDF (single page)")
    parser.add_argument("-o", "--output", required=True, help="Output PDF file")
    args = parser.parse_args()
    add_watermark(args.input, args.watermark, args.output)

if __name__ == "__main__":
    main()
