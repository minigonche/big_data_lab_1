#!/usr/bin/env python
# coding=utf-8
"""reto1_mapper.py"""
import sys
import re
#import json
#Mapper para el Reto 1 del Laboratorio 1 de Big Data

#input comes from STDIN (standard input)
for line in sys.stdin:
    if('"title"' in line):
        #Extrae el titulo
        #ajusta las dobles comillas
        line = line.replace('\\"',"'")
        resultado = re.search('"title_full": "(.*?)"', line)
        title = resultado.group(1)
        #Cuenta el numero de palabras
        # La funcion str.split() sin argumentos divide en numero
        #   de palabras
        tam = len(title.split())
        print '%s\t%s' % (title, tam)

# json solution
#for line in sys.stdin:
#    if('"title"' in line):
#        line = line.strip()
#        #Si la línea que está leyendo no está vacía
#        if line:
#            jsonObj = json.loads(line)
#            #Se obtiene el título del artículo
#            titulo = jsonObj['thread']['title_full']
#            #Número de palabras del título
#            num = len(titulo.split())
#            #Se imprime la tupla, titulo, num
#            print '%s\t%s' % (titulo, num)
