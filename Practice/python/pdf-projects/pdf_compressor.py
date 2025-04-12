#!/usr/bin/env python3
"""
pdf_compressor.py
--by yash

Compresses a PDF file using Ghostscript to reduce file size.
Usage:
    python pdf_compressor.py -i input.pdf -o compressed.pdf
Note:
    Ghostscript must be installed and accessible from the command line.
"""

import argparse
import subprocess

def compress_pdf(input_pdf, output_pdf):
    gs_command = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_pdf}",
        input_pdf
    ]
    try:
        subprocess.run(gs_command, check=True)
        print(f"Compressed PDF saved as {output_pdf}")
    except subprocess.CalledProcessError as e:
        print("Error compressing PDF:", e)

def main():
    parser = argparse.ArgumentParser(description="Compress a PDF file using Ghostscript")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file")
    parser.add_argument("-o", "--output", required=True, help="Output compressed PDF file")
    args = parser.parse_args()
    compress_pdf(args.input, args.output)

if __name__ == "__main__":
    main()
