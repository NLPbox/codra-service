#!/bin/bash
#
# usage: ./convert.sh /path/to/input.dis
# will convert /path/to/input.dis into /path/to/input.dis.png

xvfb-run ./dis2png.py $1 $1.png

