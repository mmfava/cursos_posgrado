

### 3.6 Arbolado porteño y comprensión+

### Ejercicio 3.14: Lectura de todos los árboles

def arboleda(nombre_archivo): 
    
    import csv

    f = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(f)
    headers = next(rows)

    tudo = []

    for row in rows:
        record = dict(zip(headers, row))
        tudo.append(record)
    
   
    return tudo

        
arboleda = arboleda('arboles.csv')
arboleda

### Ejercicio 3.15: Lista de altos de Jacarandá

H = [float(arbol['altura_tot']) for arbol in arboleda]
H

jacarandas = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] in {"Jacarandá"}]
jacarandas

### Exercício 3.16: Lista de alturas e diâmetros de Jacarandá

alt_diam = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] in {"Jacarandá"}]
alt_diam