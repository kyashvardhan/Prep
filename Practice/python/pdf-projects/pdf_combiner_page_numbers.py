#!/usr/bin/env python3
"""
pdf_combiner_page_numbers.py
--by yash

Combines multiple PDF files into one and adds page numbers as a footer to each page.
Usage:
    python pdf_combiner_page_numbers.py -o output.pdf input1.pdf input2.pdf ... inputN.pdf
"""

import argparse
import io
from PyPDF2 import PdfReader, PdfWriter, PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_page_number_overlay(page_width, page_height, page_number):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))
    text = f"Page {page_number}"
    can.setFont("Helvetica", 10)
    # Position near bottom center
    can.drawCentredString(page_width / 2, 20, text)
    can.save()
    packet.seek(0)
    overlay_pdf = PdfReader(packet)
    return overlay_pdf.pages[0]

def combine_pdfs_with_numbers(input_pdfs, output_pdf):
    writer = PdfWriter()
    current_page = 1
    for pdf_file in input_pdfs:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            # Create the page number overlay.
            overlay = create_page_number_overlay(page.mediabox.width, page.mediabox.height, current_page)
            page.merge_page(overlay)
            writer.add_page(page)
            current_page += 1
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Combined PDF with page numbers saved as {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Combine multiple PDFs and add page numbers")
    parser.add_argument("-o", "--output", required=True, help="Output PDF file")
    parser.add_argument("pdfs", nargs="+", help="List of PDF files to combine")
    args = parser.parse_args()
    combine_pdfs_with_numbers(args.pdfs, args.output)

if __name__ == "__main__":
    main()
