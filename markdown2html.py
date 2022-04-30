#!/usr/bin/python3
"""
This module contains script to work with the command line.
"""

if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    if os.path.exists(sys.argv[1]) is False:
        sys.stderr.write("Missing {}\n".format(sys.argv[1]))
        exit(1)
    print("")
    exit(0)
