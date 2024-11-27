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

    # Opens Markdown file then creates an HTML file.
    try:
        is_in_ul = False
        is_in_ol = False
        current_paragraph = []

        with open(file_markdown, 'r', encoding='utf-8') as file_md:
            with open(file_html, 'w', encoding='utf-8') as file_html_out:
                for line in file_md:
                    line = line.strip()

                    if line.startswith('#'):
                        heading_level = len(line.split(' ')[0])
                        if heading_level <= 6:
                            heading_content = line[heading_level:].strip()
                            file_html_out.write(
                                    f"<h{heading_level}>"
                                    f"{heading_content}</h{heading_level}>\n"
                            )
                        continue

                    if line.startswith('- '):
                        if is_in_ol:
                            file_html_out.write('<ol>\n')
                            is_in_ol = False

                        if not is_in_ul:
                            file_html_out.write('<ul>\n')
                            is_in_ul = True
                        list_item = line[2:].strip()
                        file_html_out.write(f" <li>{list_item}</li>\n")
                        continue

                    if line.startswith('* '):
                        if is_in_ul:
                            file_html_out.write('<ul>\n')
                            is_in_ul = False

                        if not is_in_ol:
                            file_html_out.write('<ol>\n')
                            is_in_ol = True
                        list_item = line[2:].strip()
                        file_html_out.write(f" <li>{list_item}</li>\n")
                        continue

                    if line:
                        current_paragraph.append(line)

                    else:
                        if current_paragraph:
                            file_html_out.write("<p>\n")
                            file_html_out.write("<br/>\n".join(current_paragraph))
                            file_html_out.write("\n</p>\n")
                            current_paragragh = []

                if current_paragraph:
                    file_html_out.write("<p>\n")
                    file_html_out.write("<br/>\n".join(current_paragraph))
                    file_html_out.write("\n</p>\n")

                if is_in_ul:
                    file_html_out.write("</ul>\n")
                if is_in_ol:
                    file_html_out.write("</ol>\n")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        exit(1)

    exit(0)
