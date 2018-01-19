#!/usr/bin/env python
import sys

with open('test.txt', 'a') as the_file:
    for x in sys.argv:
        the_file.write(x+"\t")
    the_file.write("\n")
