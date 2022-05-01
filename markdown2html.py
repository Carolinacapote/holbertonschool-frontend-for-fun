#!/usr/bin/python3
"""
This module contains script to work with the command line.
"""

if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if os.path.exists(sys.argv[1]) is False:
        sys.stderr.write("Missing {}\n".format(sys.argv[1]))
        exit(1)

    html_titles = {
        "######": ["<h6>", "</h6>"],
        "#####": ["<h5>", "</h5>"],
        "####": ["<h4>", "</h4>"],
        "###": ["<h3>", "</h3>"],
        "##": ["<h2>", "</h2>"],
        "#": ["<h1>", "</h1>"]
    }

    html_file = open(sys.argv[2], 'w')
    with open(sys.argv[1], "r") as md_file:
        lines = md_file.readlines()
        for line in lines:
            if line.startswith("#"):
                for title in html_titles:
                    if line.startswith(title):
                        html_file.write(html_titles[title][0] +
                                        line[len(title):-1] +
                                        html_titles[title][1] + "\n")
                        break
    exit(0)
