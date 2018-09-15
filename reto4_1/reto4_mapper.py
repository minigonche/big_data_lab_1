#!/usr/bin/env python
"""reto4_mapper.py"""

import sys
import re
from datetime import datetime
from datetime import timedelta
#Mapper para el Reto 4 del Laboratorio 1 de Big Data

min_date = datetime.strptime('2016-10-01','%Y-%m-%d')
max_date = datetime.strptime('2016-11-01','%Y-%m-%d')
search_word = 'Compra Euros'


# input comes from STDIN (standard input)
for line in sys.stdin:
    if('"published"' in line):
        #ajusta las dobles comillas
        line = line.replace('\\"',"'")
        #Extrae el titulo
        resultado = re.search('"published": "(.*?)"', line)
        fecha_str = resultado.group(1)

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
        #Ajusta el UTC
        try:
            hours = int(sign + utc_offset_hours)
            minutes = int(sign + utc_offset_minutes)

            fecha = fecha + timedelta(hours=hours)
            fecha = fecha + timedelta(minutes=minutes)
        except:
            raise ValueError('Bad UTC offset format: ' + utc_offset)

        # Revisa si la fecha esta entre las propuestas
        # 15 de Octubre al 15 de Noviembre
        # Si no esta en el rango imprime cero
        if(fecha < min_date or fecha > max_date):
            print '%s\t%s' % (search_word, 0)
        else:
            # Extrae el texto
            resultado = re.search('"text": "(.*?)"', line)
            texto = resultado.group(1)
            count = texto.lower().count(search_word.lower())

            print '%s\t%s' % (search_word, count)
