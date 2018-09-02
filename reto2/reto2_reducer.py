#!/usr/bin/env python
"""reto2_reducer.py"""
from operator import itemgetter
import sys
#Reducer para el Reto 2 del Laboratorio 1 de Big Data

def get_month_dict():
    months = {}
    months['January'] = 0
    months['February'] = 0
    months['March'] = 0
    months['April'] = 0
    months['May'] = 0
    months['June'] = 0
    months['July'] = 0
    months['August'] = 0
    months['September'] = 0
    months['October'] = 0
    months['November'] = 0
    months['December'] = 0

    return(months)

def export_dict(months):
    for k in months.keys():
        print '%s\t%s' % (k, months[k])


months = get_month_dict()

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    month, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # length was not a number
        raise ValueError('count was not a number: ' + str(count))

    try:
        months[month] = months[month] + count
    except:
        raise ValueError('Month key not found: ' + str(month))

#Exports month counts
export_dict(months)
