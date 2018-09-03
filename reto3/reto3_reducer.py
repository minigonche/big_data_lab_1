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
authors = []


# input comes from STDIN
for line in sys.stdin:
  
    # remove leading and trailing whitespace
    line = line.strip()
    country, author = line.split('\t', 1)

    #handles the posibility of multiple authors
    author = author.split(',')

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_country == country:
        counter = counter + 1
        authors = authors.append(author)
    else:
        if current_country:
            # write result to STDOUT
            results = {current_country : {"num_noticias": counter, "authors": authors}}
            counter = 0
       
        current_country = country
        counter = counter + 1
        authors = authors.append(author)
