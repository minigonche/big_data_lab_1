#!/usr/bin/env python

"""reto1_mapper.py"""
import sys
import re
#import json
#Mapper para el Reto 1 del Laboratorio 1 de Big Data

#input comes from STDIN (standard input)
for line in sys.stdin:
    if('"country"' in line):
        #Extrae el titulo
        #ajusta las dobles comillas
        line = line.replace('\\"',"'")
        country = re.search('"country": "(.*?)"', line)
        author = re.search('"author": "(.*?)"', line)
        country = country.group(1).strip()
        author = author.group(1).strip()

        #if there is no author, add Null
        if not author:
            author = ''

        info = "1," + author

        print('%s\t%s' % (country, info))
