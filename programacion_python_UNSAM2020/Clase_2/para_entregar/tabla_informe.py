#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 2.32 - informe

def leer_preecios(nombre_archivo):
    import csv

    precios = {}

    with open(nombre_archivo, 'rt') as f:
        for line in f:
            row = line.split(',')
            precios[row[0]] = float(row[1])
            
    return precios

precios = leer_preecios('precios.csv')

#

def leer_camion(nombre_archivo):

    import csv
    
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            lote = {'nombre':row[0], 'cajones':int(row[1]), 'precio':float(row[2])}
            camion.append(lote)
    
    return camion

camion = leer_camion('camion.csv')

## ganancias y pérdidas

def hacer_informe(camion, precios):
    tab = []
    
    for f in camion:
        for i in precios:
        
            if f['nombre'] == i:
                lista = (i, f['cajones'], f['precio'], (precios[i] - f['precio']))
                tab.append(lista)
                
    return tab

informe = hacer_informe(camion, precios)

## Tabla
print ("{:>10} {:>10} {:>10} {:>10}".format('Nombre', 'Cajones', 'Precio', 'Cambio'))
print ("{:>10} {:>10} {:>10} {:>10}".format('-------', '-------', '-------', '-------'))


for i in informe:
    a = f'${str(i[2]):.5}'
    b = (i[0], i[1], a, i[3])
    print ("{:>10s} {:>10d} {:>10.6} {:>10.2f}".format(b[0], b[1], b[2], b[3]))

