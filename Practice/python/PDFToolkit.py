import argparse
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_files, output_file):
    writer = PdfWriter()
    for pdf_path in input_files:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_file, 'wb') as f:
        writer.write(f)
    print(f"Merged {len(input_files)} files into {output_file}")


def split_pdf(input_file, output_dir):
    reader = PdfReader(input_file)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        out_path = output_dir / f"page_{i}.pdf"
        with open(out_path, 'wb') as f:
            writer.write(f)
    print(f"Split {input_file} into {len(reader.pages)} pages in {output_dir}")


def extract_metadata(input_file):
    reader = PdfReader(input_file)
    meta = reader.metadata
    print("Metadata for", input_file)
    for key, value in meta.items():
        print(f"{key}: {value}")


def add_watermark(input_file, watermark_file, output_file):
    reader = PdfReader(input_file)
    watermark = PdfReader(watermark_file).pages[0]
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(watermark)
        writer.add_page(page)
    with open(output_file, 'wb') as f:
        writer.write(f)
    print(f"Added watermark from {watermark_file} to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="PDFToolkit: merge, split, extract metadata, add watermark"
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Merge command
    merge_parser = subparsers.add_parser('merge', help='Merge multiple PDFs')
    merge_parser.add_argument('inputs', nargs='+', help='Input PDF files')
    merge_parser.add_argument('-o', '--output', required=True, help='Output PDF file')

    # Split command
    split_parser = subparsers.add_parser('split', help='Split a PDF into pages')
    split_parser.add_argument('input', help='Input PDF file')
    split_parser.add_argument('-d', '--dir', default='output_pages', help='Output directory')

    # Metadata command
    meta_parser = subparsers.add_parser('metadata', help='Extract PDF metadata')
    meta_parser.add_argument('input', help='Input PDF file')

    # Watermark command
    wm_parser = subparsers.add_parser('watermark', help='Add a watermark to a PDF')
    wm_parser.add_argument('input', help='Input PDF file')
    wm_parser.add_argument('watermark', help='PDF file containing watermark page')
    wm_parser.add_argument('-o', '--output', required=True, help='Output PDF file')

    args = parser.parse_args()

    if args.command == 'merge':
        merge_pdfs(args.inputs, args.output)
    elif args.command == 'split':
        split_pdf(args.input, args.dir)
    elif args.command == 'metadata':
        extract_metadata(args.input)
    elif args.command == 'watermark':
        add_watermark(args.input, args.watermark, args.output)

if __name__ == '__main__':
    main()
