#!/usr/bin/env python
# coding=utf-8
"""reto4_reducer.py"""
#TODO

import sys

# input comes from STDIN (standard input)
item = None
current_item = None
current_count = 0
#Lectura del resultado del mapper
for line in sys.stdin:
    #elimina el salto de línea
    line = line.strip()
    item, count = line.split('\t')

    #se convierte el count a un entero
    try:
        count = int(count)
    except ValueError:
        #Continúe a la siguiente iteración
        continue
    #Si el ítem actual es igual al analizado
    #aumenta el contador en count (+count)
    if current_item == item:
        current_count += count
    else:
        #Si el ítem es diferente al analizado
        #se setea item y count
        current_item = item
        current_count = count
#Ultima iteración
#Se imprimen valores finales del conteo
if item:
    if current_item == item:
        print '%s\t%s' % (current_item, current_count)
