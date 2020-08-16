
## Ejercicio 3.2: Búsquedas de un elemento


def buscar_u_elemento(lista, e):

    pos = -1  
    for i, z in enumerate(lista): 
        if z == e:   
            pos = i  
            pass   
            
    return pos


print(buscar_u_elemento([1,2,3,2,3,4],1))
print(buscar_u_elemento([1,2,3,2,3,4],2))
print(buscar_u_elemento([1,2,3,2,3,4],3))
print(buscar_u_elemento([1,2,3,2,3,4],5))

## ¿Por qué falla en el último caso? Porque m = 0 y 0 es mayor que -5 y -4.
## ¿Por qué anda en el caso anterior? El 'pos', que sería equivalente al 'm', no se usó para comparación, solo como un valor de salida.
## ¿Cómo se puede inicializar m para que la función ande también con números negativos? Considerando m como un número infinito negativo
## Corregilo y guarda la versión mejorada en el archivo

#%%

## Ejercicio 3.3: Búsqueda de máximo y mínimo

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    
    m = float('-inf') 
    
    for e in lista:
        if e > m:
            m = e  
            
        elif e < 0 and m <= 0 and e > m:
            m = e
        
    return m

print(maximo([1,2,7,2,3,4]))
print(maximo([1,2,3,4]))
print(maximo([-5, 4]))
print(maximo([-5,-4, -1, -2, -10]))


