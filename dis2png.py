#!/usr/bin/env python2.7

import argparse
import base64
import os
import sys

from nltk.draw.tree import TreeView
from discoursegraphs.readwrite.rst.dis.distree import DisRSTTree


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('input_file', help="path to RST tree (.dis format)")
    parser.add_argument('output_file', help="path to output file (base64 png string format)")

    args = parser.parse_args(sys.argv[1:])

    t = DisRSTTree(args.input_file, word_wrap=20)

    base64_pngstr = t._repr_png_()
    with open(args.output_file, 'wb') as outfile:
        outfile.write(base64_pngstr)

