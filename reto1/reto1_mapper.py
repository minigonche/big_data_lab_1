#!/usr/bin/env python
"""reto1_mapper.py"""

import sys
import re
#Mapper para el Reto 1 del Laboratorio 1 de Big Data

# input comes from STDIN (standard input)
for line in sys.stdin:
    if('"title"' in line):
        #Extrae el titulo
        resultado = re.search('"title": "(.*?)"', line)
        title = resultado.group(1)
        #Cuenta el numero de palabras
        # La funcion str.split() sin argumentos divide en numero
        #   de palabras
        tam = len(title.split())

        print '%s\t%s' % (title, tam)
