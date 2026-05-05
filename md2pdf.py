#!/usr/bin/env python3
import argparse
import os
import sys

import markdown
from weasyprint import HTML


def generate_pdf(input_md_file, output_pdf_file):
    # Read the Markdown file
    try:
        with open(input_md_file, "r", encoding="utf-8") as f:
            md_content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_md_file}' was not found.")
        sys.exit(1)

    # Convert Markdown to HTML (enabling tables and code blocks)
    html_content = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

    # Define the CSS styling
    css_style = """
    <style>
    @page {
        size: A4;
        margin: 20mm;
        background-color: #fcfbfa;
    }
    body {
        font-family: 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #2d3748;
        font-size: 10.5pt;
        line-height: 1.6;
        background-color: #fcfbfa;
    }
    h1 { color: #1a202c; border-bottom: 2px solid #a0aec0; padding-bottom: 8px; margin-bottom: 24px; font-size: 22pt; }
    h2 { color: #2b6cb0; margin-top: 30px; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; font-size: 16pt; }
    h3 { color: #2c5282; font-size: 13pt; margin-top: 20px;}
    pre {
        background-color: #1e293b;
        color: #f8fafc;
        padding: 12px;
        border-radius: 6px;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 9pt;
        overflow-x: auto;
    }
    code {
        background-color: #e2e8f0;
        padding: 2px 4px;
        border-radius: 4px;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 9.5pt;
        color: #b91c1c;
    }
    pre code {
        padding: 0;
        background-color: transparent;
        color: inherit;
        border: none;
    }
    ul { list-style-type: disc; padding-left: 20px; }
    li { margin-bottom: 4px; }
    hr { border: 0; border-top: 1px solid #cbd5e1; margin: 24px 0; }
    table { width: 100%; border-collapse: collapse; margin-top: 15px; margin-bottom: 15px; }
    th, td { border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left; }
    th { background-color: #f1f5f9; font-weight: 600; }
    </style>
    """

    full_html = f"<!DOCTYPE html><html><head>{css_style}</head><body>{html_content}</body></html>"

    # Generate the PDF
    print(f"Generating PDF from '{input_md_file}'...")
    try:
        HTML(string=full_html).write_pdf(output_pdf_file)
        print(f"Success! PDF saved as: {output_pdf_file}")
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")


if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file to a professionally styled PDF."
    )
    parser.add_argument(
        "input_file", help="Path to the input Markdown file (e.g., document.md)"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Optional: Path for the output PDF file. If omitted, uses the input filename.",
        default=None,
    )

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output

    # Automatically generate output filename if not provided
    if not output_file:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}.pdf"

    generate_pdf(input_file, output_file)
