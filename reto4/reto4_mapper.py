#!/usr/bin/env python
# coding=utf-8
"""reto4_mapper.py"""
#TODO
import sys
import re
import json
from datetime import datetime
from datetime import timedelta

#Mapper para el Reto 1 del Laboratorio 1 de Big Data

# input comes from STDIN (standard input)
#sys.stdin devuelve la entrada (palabras o archivo)
for line in sys.stdin:
    line = line.strip()
    if('text' in line):
        #Si la línea que está leyendo no está vacía
        if line:
            print '** línea con contenido **'
            jsonObj = json.loads(line)
            #Se obtiene el título del artículo
            body = jsonObj['text']
            #Número de palabras del título
            num = len(body.split())
            #Se imprime la tupla, titulo, num
            print num
            # Encuentra las palabras 'Compra Euros' del body
            search = "Compra Euros"
            print re.findall(r"\b" + search + r"\b", body)
