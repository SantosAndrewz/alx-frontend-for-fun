#!/usr/bin/python3
"""
Module converts a Markdown file to an HTML file.
"""


import os
import sys

if __name__ == "__main__":
    # Checks the number of arguments entered.
    if len(sys.argv) < 3:
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr
        )
        exit(1)

    file_markdown = sys.argv[1]
    file_html = sys.argv[2]

    # Checks for presence of Markdown file.
    if not os.path.exists(file_markdown):
        print(f"Missing {file_markdown}", file=sys.stderr)
        exit(1)

    # Opens Markdown file then creates an empty file.
    try:
        with open(file_markdown, 'r', encoding='utf-8') as file_md:
            md_content = file_md.read()
        with open(file_html, 'w', encoding='utf-8') as file_html_out:
            file_html_out.write("")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        exit(1)

    exit(0)