#!/usr/bin/env python
"""reto2_mapper.py"""

import sys
import re
from datetime import datetime
from datetime import timedelta
#Mapper para el Reto 2 del Laboratorio 1 de Big Data

# input comes from STDIN (standard input)
for line in sys.stdin:
    if('"published"' in line):
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

        month = fecha.strftime("%B")

        print '%s\t%s' % (month, 1)
