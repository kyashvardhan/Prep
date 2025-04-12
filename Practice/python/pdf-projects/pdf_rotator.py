#!/usr/bin/env python3
"""
pdf_rotator.py
--by yash
Rotates all pages of an input PDF by a specified angle.
Usage:
    python pdf_rotator.py -i input.pdf -o rotated.pdf -a 90
"""

import argparse
from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf(input_pdf, output_pdf, angle):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Rotated PDF saved as {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Rotate PDF pages by a specified angle")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file")
    parser.add_argument("-o", "--output", required=True, help="Output PDF file")
    parser.add_argument("-a", "--angle", type=int, required=True, help="Rotation angle (in degrees)")
    args = parser.parse_args()
    rotate_pdf(args.input, args.output, args.angle)

if __name__ == "__main__":
    main()
