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
for line in sys.stdin:
    line = line.strip()
    #Realiza el procedimiento solo si encuentra 'text'
    if('text' in line):
        #Si la línea que está leyendo no está vacía
        if line:
            #parsea lectura (string) a json
            jsonObj = json.loads(line)
            #Se obtiene la fecha
            fecha_str = jsonObj['published']
            # Covierte a fecha
            # Python 2 no tiene soporte para utc offset
            utc_offset = fecha_str[-6:]
            utc_offset_hours = fecha_str[-5:-3]
            utc_offset_minutes = fecha_str[-2:]
            sign = fecha_str[-6]
            fecha_str = fecha_str[:-6]
            # Formato
            format = '%Y-%m-%dT%H:%M:%S.%f'
            fecha = datetime.strptime(fecha_str,format)
            #2016-10-02 11:00:00   
            #Ajusta el UTC
            try:
                hours = int(sign + utc_offset_hours)
                minutes = int(sign + utc_offset_minutes)
                fecha = fecha + timedelta(hours=hours)
                fecha = fecha + timedelta(minutes=minutes)
                #Fecha de inicio y fin del filtro
                start = datetime(2016, 6, 15) #aaaa-mm-dd
                end = datetime(2016, 10, 15) #aaaa-mm-dd
                #Palabra a buscar en el body 'Compra Euros'
                search = 'Compra Euros'#"Compra Euros"
                #Archivo dentro del rango de fechas - print "in between"
                if start <= fecha <= end:
                    #Se obtiene el título del artículo
                    body = jsonObj['text']
                    #Número de palabras del título
                    num = len(body.split())#for debug test
                    
                    result = re.findall(r"\b" + search + r"\b", body)
                    if(len(result)>0):
                        for matchword in result:
                            print '%s\t%s' % (matchword, 1)
                    else:
                        print '%s\t%s' % (search, 0)
                else:
                    #Imprime la palabra con el valor de cero
                    #cuando ni siquiera el archivo se publicó 
                    #en el rango de fechas seleccionadas.
                    print '%s\t%s' % (search, 0)
            except:
                raise ValueError('Bad UTC offset format: ' + utc_offset)

            


