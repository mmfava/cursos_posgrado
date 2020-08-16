
## Ejercicio 3.4: Invertir una lista

def invertir_lista(lista):
    invertida = []
    i = -1
    for e in lista: 
        invertida.insert(i, e)
        i -= 1
        
    return invertida

print(invertir_lista([1,2,3,4,5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 
                      'San Fernando', 'San Miguel']))