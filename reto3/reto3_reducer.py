#!/usr/bin/env python
"""reto3_reducer.py"""
#TODO

'''
Reducer para el reto 3 del laboratorio 1.

Enunciado:
Para cada pais en el cual se publican las noticias,
indique cuantas noticias se publican y ciales so los autores de las noticias
de ese pais
'''

import sys
import json

counter = 0
current_country = None
authors = ''

# input comes from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()
    country, body = line.split('\t', 1)
    count, author = body.split(',', 1)
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_country == country:
        counter = counter + int(count)
        if (author) and (author not in authors):
            if authors == '':
                authors = ''.join([authors, author])
            else:
                authors = ','.join([authors, author])
    else:
        if current_country:
            # write result to STDOUT
            info = str(counter) + "," + authors
            print('%s\t%s' % (current_country, info))
            authors = ''
            counter = 0


        current_country = country
        counter = counter + int(count)
        if (author) and (author not in authors):
            if authors == '':
                authors = ''.join([authors, author])
            else:
                authors = ','.join([authors, author])

# do not forget to output the last word if needed!
if current_country == country:
        info = str(counter) + "," + authors
        print('%s\t%s' % (current_country, info))
