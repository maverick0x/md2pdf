# md2pdf

A simple, robust command-line tool to convert Markdown (`.md`) files into professionally styled PDF documents. Works seamlessly across Linux, macOS, and Windows.

## Features
* **Beautiful Default Styling:** Automatically formats headings, code blocks, tables, and lists.
* **Batch Processing:** Convert multiple Markdown files at once or use wildcards to convert entire directories.
* **Cross-Platform:** Installs as a native command-line tool on your OS.
* **Markdown Extensions:** Native support for tables and fenced code blocks.

## Prerequisites

Before installing `md2pdf`, ensure you have **Python 3.x** installed. 
* *Windows Users:* Make sure to check "Add Python to PATH" during installation.

**WeasyPrint Dependencies:**
This tool uses WeasyPrint to generate PDFs. Depending on your operating system, you may need to install underlying graphics libraries:
* **Linux (Ubuntu/Debian):** `sudo apt install libpango-1.0-0 libpangoft2-1.0-0`
* **macOS:** `brew install pango`
* **Windows:** WeasyPrint requires GTK3. You can download and run the latest GTK3 installer from the [WeasyPrint documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows). Ensure you check the box to add GTK to your system PATH during installation.

## Installation

You can install `md2pdf` globally on your system using Python's package manager, `pip`.

**Clone or download this repository:**
```bash
git clone https://github.com/maverick0x/md2pdf.git
cd md2pdf
```

**Install the package using `pip`**
```bash
pip install .
```
*(Note: The dot `.` at the end is required. It tells pip to install the package from the current directory).*

**Verify the installation:**
```bash
md2pdf --help
```

## Usage
Once installed, you can run `md2pdf` from anywhere in your terminal or command prompt!

### Convert a single Markdown file to PDF:
```bash
md2pdf document.md
```
This will generate a document.pdf in the same directory.

### Specify a Custom Output Name
Use the `-o` or `--output` flag to specify exactly what the final PDF should be named. *(Note: This flag is ignored if you are converting multiple files at once).*
```bash
md2pdf document.md -o my_custom_report.pdf
```

### Convert Multiple Specific Files
Use wildcard characters to convert all markdown files in your current folder instantly.
```bash
md2pdf file1.md file2.md file3.md
```
This will create file1.pdf, file2.pdf, and file3.pdf in the same directory

### Convert All Markdown Files in a Directory
```bash
md2pdf *.md
```
This will convert all `.md` files in the current directory to PDFs.

## Troubleshooting
If your terminal says `md2pdf is not recognized` (or `command not found`) after installation, your Python Scripts folder is likely not in your system's PATH.

Windows: Add `%USERPROFILE%\AppData\Local\Programs\Python\Python3x\Scripts` to your system Environment Variables.

Linux/macOS: Add export `PATH="$HOME/.local/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc` file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
