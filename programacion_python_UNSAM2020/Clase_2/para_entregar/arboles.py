#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Lectura de los árboles de un parque

def leer_parque(nombre_archivo, parque): 
    
    import csv

    f = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(f)
    headers = next(rows)

    tudo = []
    lista = []

    for row in rows:
        record = dict(zip(headers, row))
        tudo.append(record)
    
    for i in tudo:
        if i['espacio_ve'] == parque:
            # print ("{:<10} {:<10} {:<10}".format()) 
            lista.append(i)
    
    return lista

        
gen_paz = leer_parque('arboles.csv', 'GENERAL PAZ')
gen_paz

### Ejercicio 2.23: Determinar las especies en un parque

def especies(parque):
    
    nombres = [] 
    
    for i in parque:
        nombres.append(i['nombre_com']) 
    
    unique = set(nombres)
    
    return [list(unique), nombres]

lista_arboles_gp = especies(gen_paz)

lista_arboles_gp[0] # lista de especies con valores únicos
lista_arboles_gp[1] # lista con todas las ocurrencias

### Ejercicio 2.24: Contar ejemplares por especie

## Parte I:
def contar_ejemplares(lista_arboles):
    
    from collections import Counter

    contar = Counter(lista_arboles)
    
    return contar

freq_gp = contar_ejemplares(lista_arboles_gp[1])
freq_gp

## Parte II
los_andes = leer_parque('arboles.csv', 'CENTENARIO')
lista_arboles_la = especies(los_andes)
freq_la = contar_ejemplares(lista_arboles_la[1])

centenario = leer_parque('arboles.csv', 'CENTENARIO')
lista_arboles_centenario = especies(centenario)
freq_centenario = contar_ejemplares(lista_arboles_centenario[1])

print(freq_gp.most_common(5), ' \n')

print(freq_la.most_common(5), ' \n')

print(freq_centenario.most_common(5), ' \n')

