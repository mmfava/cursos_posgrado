#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# costo_camion_commandline.py

import sys
import csv

def costo_camion(nombre_archivo): 

    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)

    total = 0
    
    for row in rows:
        try:
            total += int(row[1]) * float(row[2])
            print(row, total)
        except:
            total += float(row[2])
            print('Valores faltantes em', row)
            print(row, total)

                            
    return round(total, 2)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'


costo = costo_camion(nombre_archivo)
print('Costo total: ', costo)

