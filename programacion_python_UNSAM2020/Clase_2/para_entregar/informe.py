#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
gan_perd = []

for f in camion:
    for i in precios:
        
        if f['nombre'] == i:
            gan_perd = (precios[i] - f['precio']) * f['cajones']
            
            if gan_perd < 0:
                print("======= ", i, " =======")
                print('Monto pagado al productor: ', (f['precio'] * f['cajones']))
                print('Valor comercial del producto: ', precios[i], "/unidad" )
                print('Diferencia por unidad: $', precios[i] - f['precio'])
                print('Resultó en una pérdida de dinero: $', gan_perd)
                print("")
            
            else:
                print("======= ", i, " =======")
                print('Monto pagado al productor: ', round((f['precio'] * f['cajones']), 2))
                print('Valor comercial del producto: ', precios[i], "/unidad" )
                print('Diferencia por unidad: $', round((precios[i] - f['precio']), 2))
                print('Resultó en ganancia de dinero: $', round(gan_perd, 2))
                print('')     
                

