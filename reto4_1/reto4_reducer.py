#!/usr/bin/env python
"""reto4_reducer.py"""

from operator import itemgetter
import sys
#Reducer para el Reto 4 del Laboratorio 1 de Big Data

global_count = 0
#version simple del word count
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except:
        raise ValueError('Count is not a number')

    global_count = global_count + count

print '%s\t%s' % (word, global_count)
