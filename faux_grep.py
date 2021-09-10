import fileinput
import sys
import re
from argparse import ArgumentParser

# python faux_grep.py -i -H  bird DATA/alice.txt DATA/words.txt ...

parser = ArgumentParser(description="Faux grep")

parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("-H", dest="show_files", action="store_true", help="Show file name")
parser.add_argument("search_term", help="Regex to match", metavar="search term")
parser.add_argument("files", nargs="*", help="Files to search (STDIN if no files specified")

args = parser.parse_args()
print(args, '\n')

for line in fileinput.input(args.files):
    if re.search(args.search_term, line, re.I if args.ignore_case else 0):
        line = line.rstrip()
        if args.show_files:
            print(fileinput.filename(), end=' ')
        print(line)

