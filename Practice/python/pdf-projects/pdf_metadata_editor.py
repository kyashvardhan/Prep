#!/usr/bin/env python3
"""
pdf_metadata_editor.py
--by yash

Edits the metadata of a PDF file.
Usage:
    python pdf_metadata_editor.py -i input.pdf -o output.pdf --title "New Title" --author "Author Name" --subject "Subject Info"
"""

import argparse
from PyPDF2 import PdfReader, PdfWriter

def edit_metadata(input_pdf, output_pdf, title, author, subject):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    metadata = reader.metadata or {}
    if title:
        metadata.update({"/Title": title})
    if author:
        metadata.update({"/Author": author})
    if subject:
        metadata.update({"/Subject": subject})
    writer.add_metadata(metadata)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Updated metadata PDF saved as {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Edit metadata of a PDF")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file")
    parser.add_argument("-o", "--output", required=True, help="Output PDF file")
    parser.add_argument("--title", type=str, default="", help="New Title")
    parser.add_argument("--author", type=str, default="", help="New Author")
    parser.add_argument("--subject", type=str, default="", help="New Subject")
    args = parser.parse_args()
    edit_metadata(args.input, args.output, args.title, args.author, args.subject)

if __name__ == "__main__":
    main()
