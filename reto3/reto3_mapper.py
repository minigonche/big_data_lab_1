#!/usr/bin/env python
"""reto3_mapper.py"""
#TODO
'''
Mapper para el reto 3 del laboratorio 1.

Enunciado:
Para cada pais en el cual se publican las noticias,
indique cuantas noticias se publican y ciales so los autores de las noticias
de ese pais
'''

import sys
import json

for line in sys.stdin:
    line = line.strip()
    if line:
        data = json.loads(line)
        country = data_j.get('thread').get('country')
        author = data_j.get('author')

        # if there are several authors, join them as a single csv string
        if author.__class__ == list:
            author = ",".join(author)

        results = [country, author]
        print("\t".join(results))
