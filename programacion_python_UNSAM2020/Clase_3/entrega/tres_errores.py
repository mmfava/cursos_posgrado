## 3.1:
    
## 1. Error semántico: Fue posible ejecutar el código inicial, pero el resultado no salió como se esperaba.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    tiene = False 
    
    while i<n and not tiene:
        if expresion[i] == 'a' or 'A': # !No recordaba si era necesario identificar las mayúsculas y minúsculas; pero, por las dudas...
            tiene = True
        i += 1
    return tiene

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
## 2. el código tiene varios errores de "escritura", lo que hace imposible ejecutar la función.

def tiene_a(expresion):
    
    n = len(expresion)
    i = 0
    tiene = False
    
    while i<n and not tiene:
        if expresion[i] == 'a'or 'A':
            tiene = True
        i += 1
    return tiene


print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
## tiempo de ejecución: Cuando el programa empieza a ejecutarse pero se produce un error durante su ejecución. 
##                      En este caso específico, 1984 se escribió como un valor numérico, no como una string.

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno('1984'))



