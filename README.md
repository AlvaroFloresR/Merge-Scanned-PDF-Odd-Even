# Merge Scanned PDF with 2 files Odd and Even Pages

## The Issue
Let's say you have 300 2-Sided pages you want to scan into a single file using the "Document Feeder" of your scanner. You could face 3 issues:
1. The scanner is extremely slow while scanning a 2-sided document
2. The scanner only accepts Letter or A4 sizes for 2-sided scan
3. Your scanner can only scan 1-sided documents

## The Solution
Scan 2 files:
- The first one for "Odd Pages" (1, 3, 5, 7...)
- The second for "Even Pages" (300, 298, 296...)
  - *This happens when you scan the entire block of pages. This script reverses this order*

You would feed your scanner:
1. First the block of pages "upside up" to get the "Odd Pages" (1, 3, 5, 7...)
2. Then you would flip around the **entire** block of pages and feed them "upside down" to get the "Even Pages" (300, 298, 296...)
    - *NOTE: **Don't** flip around each page, the purpose of this script is to avoid that*

## Script Pre-Requirements
1. PyPDF2 Package https://pypi.org/project/PyPDF2/
2. 2 PDF Files called: "odd.pdf" and "even.pdf"

## How to Use it?
1. Place the script in the same folder as the 2 PDF files
2. Run the script
